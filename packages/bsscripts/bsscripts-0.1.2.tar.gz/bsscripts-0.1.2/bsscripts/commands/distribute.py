import logging
import shutil

from bsscripts.commands import APICommand
from bsscripts.division.brightspace import BrightspaceDivider
from bsscripts.division.persistent import PersistentDivider
from bsscripts.division.random import RandomDivider
from bsscripts.download import Downloader
from bsscripts.emails import EmailNotifier
from bsscripts.processing import NOPProcessing, SubmissionsProcessing, GraderProcessing
from bsscripts.processing.graders.create_archive import (
    MoveToGraderFolder,
    CreateGraderArchives,
)
from bsscripts.processing.graders.feedback_template import CreateFeedbackTemplate
from bsscripts.processing.graders.grader_config import CreateGraderConfig
from bsscripts.processing.graders.grading_instructions import (
    InjectGraderFiles,
    AddGraderFiles,
    CreateGradingInstructions,
)
from bsscripts.processing.submissions.docx_to_pdf import DocxToPdf
from bsscripts.processing.submissions.extract_archives import ExtractArchives
from bsscripts.processing.submissions.fix_permissions import FixFilePermissions
from bsscripts.processing.submissions.flatten import Flatten, SmartFlatten
from bsscripts.processing.submissions.inject_files import InjectFiles
from bsscripts.processing.submissions.remove_files import RemoveFiles
from bsscripts.progress import Report
from bsscripts.scp import SCPUploader

logger = logging.getLogger(__name__)


class DistributeCommand(APICommand):
    def __init__(self):
        super().__init__(["distribute"], "Distribute an assignment")
        self.add_positional_arg(
            "assignment-id",
            "The assignment identifier",
            self.app.is_valid_assignment_id,
        )
        self.add_flag_arg("no-upload", "Do not run uploader and notifier")
        self.add_flag_arg("no-notify", "Do not run notifier")
        self.add_flag_arg(
            "no-confirm", "Do not ask for confirmation before running notifier"
        )

    def execute_api(self):
        do_not_upload = self.get_flag_arg("no-upload")
        do_not_notify = self.get_flag_arg("no-notify") or do_not_upload
        do_confirm = not self.get_flag_arg("no-confirm")

        assignment_id = self.get_positional_arg(0)
        assignment_config = self.config.assignments[assignment_id]
        root_path = self.app.root_path
        stage_path = root_path / "stage"
        submissions_path = stage_path / "submissions"
        graders_path = stage_path / "graders"
        data_path = root_path / "data"
        inject_path = data_path / "inject"
        grader_data_path = self.app.package_data_path / "grader"
        course_path = data_path / "course" / self.config.course
        distributions_path = root_path / "distributions"
        logs_path = root_path / "logs"

        downloader = Downloader(
            self.api, self.config, root_path, Report("Download submissions")
        )
        assignment_info = downloader.download(assignment_id)
        if assignment_info is None:
            logger.fatal("Failed to download submissions, abandoning distribution")
            return

        division_method = assignment_config.division.method
        assert division_method in [
            "random",
            "persistent",
            "brightspace",
            "custom",
        ], f'unknown division method "{division_method}"'
        match division_method:
            case "random":
                divider = RandomDivider(self.config)
            case "persistent":
                divider = PersistentDivider(self.config, data_path)
            case "brightspace":
                divider = BrightspaceDivider(self.api, self.config)
            case "custom":
                divider = self.app.course_plugin.get_divider(assignment_id)
            case _:
                assert False, "Unreachable"

        if not divider.initialize(assignment_info):
            logger.fatal("Failed to initialize divider, abandoning distribution")
            return
        division = divider.divide(assignment_info)
        division.write_logs(logs_path / assignment_id)

        file_hierarchy = assignment_config.file_hierarchy
        assert file_hierarchy in [
            "flatten",
            "smart",
            "original",
        ], f'unknown file hierarchy "{file_hierarchy}"'
        match file_hierarchy:
            case "flatten":
                file_hierarchy_pass = Flatten(Report("Flatten files"))
            case "smart":
                file_hierarchy_pass = SmartFlatten(Report("Smart flatten files"))
            case "original":
                file_hierarchy_pass = NOPProcessing()
            case _:
                assert False, "Unreachable"

        submission_passes: list[SubmissionsProcessing] = [
            ExtractArchives(Report("Extract archives")),
            FixFilePermissions(Report("Fix file permissions")),
            RemoveFiles(assignment_config, Report("Remove files")),
            DocxToPdf(Report("Convert DOCX to PDF")),
            file_hierarchy_pass,
            InjectFiles(assignment_config, inject_path, Report("Inject files")),
            CreateFeedbackTemplate(
                assignment_info, Report("Create feedback templates")
            ),
            MoveToGraderFolder(division, graders_path, Report("Move to graders")),
        ]
        grader_passes: list[GraderProcessing] = [
            InjectGraderFiles(
                assignment_config, inject_path, Report("Inject grader files")
            ),
            AddGraderFiles(
                grader_data_path, course_path, Report("Add grader files")
            ),
            CreateGraderConfig(
                division,
                assignment_info,
                self.config,
                self.app.api_config,
                assignment_config,
                Report("Create grader configs"),
            ),
            CreateGradingInstructions(
                assignment_info,
                assignment_config,
                Report("Create grading instructions"),
            ),
            CreateGraderArchives(
                distributions_path, assignment_config, Report("Create grader archives")
            ),
        ]

        submission_passes = self.app.course_plugin.modify_submission_passes(
            submission_passes
        )
        grader_passes = self.app.course_plugin.modify_grader_passes(grader_passes)

        for pass_ in submission_passes:
            pass_.execute(submissions_path)
        for pass_ in grader_passes:
            pass_.execute(graders_path)

        if do_not_upload:
            return

        print("Uploading files to remote share...")
        uploader = SCPUploader(distributions_path, logs_path, self.config)
        if not uploader.upload(assignment_id):
            logger.fatal(
                "Failed to upload to distribution share, abandoning distribution"
            )
            return

        if do_not_notify:
            return

        notifier = EmailNotifier(
            distributions_path,
            self.config,
            self.app.smtp_config,
            assignment_info,
            division,
            Report("Send grader notifications"),
        )
        notifier.create_notifications()

        # Ask before sending notifications in case it went tits up.
        # This way we can fix it and re-run the distribution before sending notifications out to the graders.
        if do_confirm and input("Send notifications? [y/n]: ").strip().lower() in [
            "y",
            "yes",
        ]:
            if notifier.initialize():
                notifier.send_notifications()
                notifier.shutdown()
            else:
                logger.fatal("Failed to initialize notifier, no notifications sent")
            shutil.rmtree(stage_path, ignore_errors=True)
        else:
            print("Not sending notifications; stage folder still exists for debugging")
