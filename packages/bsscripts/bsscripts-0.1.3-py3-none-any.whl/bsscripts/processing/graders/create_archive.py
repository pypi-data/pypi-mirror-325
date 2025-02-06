import logging
import secrets
import shutil
import string
import subprocess
from pathlib import Path

from bsscripts.config import AssignmentConfig
from bsscripts.division import Division
from bsscripts.processing import SubmissionsProcessing, GraderProcessing
from bsscripts.progress import ProgressReporter

logger = logging.getLogger(__name__)


class MoveToGraderFolder(SubmissionsProcessing):
    def __init__(
        self,
        division: Division,
        graders_path: Path,
        progress_reporter: ProgressReporter = None,
    ):
        super().__init__(progress_reporter)
        self.submission_to_grader: dict[str, str] = dict()
        self.graders_path = graders_path

        for grader_id, submissions in division:
            for submission in submissions:
                self.submission_to_grader[submission.folder_name] = grader_id

            grader_path = graders_path / grader_id / "submissions"
            grader_path.mkdir(parents=True, exist_ok=True)

    def process_submission(self, submission_path: Path):
        grader_id = self.submission_to_grader[submission_path.name]
        grader_path = self.graders_path / grader_id / "submissions"
        shutil.move(submission_path, grader_path)


class CreateGraderArchives(GraderProcessing):
    def __init__(
        self,
        dist_path: Path,
        assignment_config: AssignmentConfig,
        progress_reporter: ProgressReporter = None,
    ):
        super().__init__(progress_reporter)
        self.dist_path = dist_path
        self.assignment_config = assignment_config

    def process_grader(self, grader_path: Path):
        grader_id = grader_path.name
        assignment_id = self.assignment_config.identifier

        # Create target file path, and ensure parent folders exists.
        parent_path = self.dist_path.resolve() / assignment_id
        archive_path = parent_path / f"{assignment_id}-{grader_id}.7z"
        password_path = parent_path / f"{assignment_id}-{grader_id}.password"
        parent_path.mkdir(parents=True, exist_ok=True)

        # Generate random password using CS-PRNG.
        alphabet = string.ascii_letters + string.digits
        password_length = 32
        password = "".join(secrets.choice(alphabet) for _ in range(password_length))
        password_path.write_text(password, encoding="utf-8")

        # 'a'      => Add files to archive command.
        # '-ms=on' => Turn on solid mode (groups files together for potentially better compression).
        # '-mx=9'  => Use Ultra compression level.
        # '-mhe'   => Encrypt archive header to hide file table as file name may still expose student info like names/student numbers.
        # This creates an archive using AES-256-CBC encryption, and a PBKDF based on 2^19 SHA256 iterations.
        args = [
            "7za",
            "a",
            "-ms=on",
            "-mx=9",
            "-mhe",
            f"-p{password}",
            archive_path,
            "./",
        ]
        try:
            cp = subprocess.run(
                args, shell=False, check=False, capture_output=True, cwd=grader_path
            )
            if cp.returncode != 0:
                logger.fatal(
                    'Creating archive failed with exit code %d and stderr output "%s"',
                    cp.returncode,
                    cp.stderr,
                )
        except FileNotFoundError:
            logger.fatal("Creating archive failed as 7-Zip was not found")
