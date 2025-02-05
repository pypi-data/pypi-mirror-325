import json
import logging
from pathlib import Path

import bsapi

from bsscripts.config import AssignmentConfig, Config
from bsscripts.division import Division
from bsscripts.download import AssignmentInfo
from bsscripts.processing import GraderProcessing
from bsscripts.progress import ProgressReporter

logger = logging.getLogger(__name__)


class CreateGraderConfig(GraderProcessing):
    def __init__(
        self,
        division: Division,
        assignment_info: AssignmentInfo,
        config: Config,
        api_config: bsapi.APIConfig,
        assignment_config: AssignmentConfig,
        progress_reporter: ProgressReporter = None,
    ):
        super().__init__(progress_reporter)
        self.division = division
        self.assignment_info = assignment_info
        self.config = config
        self.api_config = api_config
        self.assignment_config = assignment_config

    def process_grader(self, grader_path: Path):
        submissions_info = self.division[grader_path.name]
        data_path = grader_path / "data"
        config_path = data_path / "config.json"
        grader_info = self.config.graders[grader_path.name]

        grade_object = self.assignment_info.grade_object
        grade_scheme = self.assignment_info.grade_scheme

        data_path.mkdir(parents=True, exist_ok=True)
        with open(config_path, "w", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "orgUnitId": self.assignment_info.course.org_unit.id,
                        "folderId": self.assignment_info.assignment.id,
                        "groupCategoryId": self.assignment_info.assignment.group_type_id,
                        "assignmentId": self.assignment_config.identifier,
                        "defaultCodeBlockLanguage": self.assignment_config.default_code_block_language,
                        "draftFeedback": self.assignment_config.draft_feedback,
                        "gradedByFooter": self.assignment_config.graded_by_footer,
                        "tag": self.config.tag,
                        "grader": {
                            "name": grader_info.name,
                            "email": grader_info.contact_email,
                        },
                        "grade": {
                            "name": grade_object.name,
                            "type": grade_object.grade_type,
                            "aliases": self.assignment_config.grade_aliases,
                            "maxPoints": self.assignment_info.assignment.assessment.score_denominator,
                            "objectMaxPoints": grade_object.max_points,
                            "symbols": [r.symbol for r in grade_scheme.ranges],
                        },
                        "api": self.api_config.to_json(),
                        "submissions": {
                            info.folder_name: {
                                "entityId": info.entity_id,
                                "entityType": info.entity_type,
                                "submissionId": info.submission_id,
                                "submittedBy": int(info.submitted_by.identifier),
                                "students": {
                                    int(student.identifier): {
                                        "name": student.display_name,
                                        "username": student.user_name,
                                    }
                                    for student in info.students
                                },
                            }
                            for info in submissions_info
                        },
                    },
                    indent=4,
                    ensure_ascii=False,
                )
            )
