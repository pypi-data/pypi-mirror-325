import datetime
import logging

import bsapi
import bsapi.helper
import bsapi.types

from bsscripts.commands import AppCommand, APICommand
from bsscripts.utils import (
    TablePrinter,
    format_datetime,
    format_timedelta,
    to_local_time,
)

logger = logging.getLogger(__name__)


class ListGradersCommand(AppCommand):
    def __init__(self):
        super().__init__(["list", "graders"], "List all graders")

    def execute(self):
        table = TablePrinter()
        table.add_column("identifier")
        table.add_column("name")
        table.add_column("contact")
        table.add_column("username")
        table.add_column("distribute")

        for grader_id, grader in self.app.config.graders.items():
            table.add_row(
                [
                    grader_id,
                    grader.name,
                    grader.contact_email,
                    grader.distribute_username,
                    grader.distribute_email,
                ]
            )

        table.print()


class ListAssignmentsCommand(APICommand):
    def __init__(self):
        super().__init__(["list", "assignments"], "List all assignments")

    def execute_api(self):
        table = TablePrinter()
        table.add_column("identifier")
        table.add_column("name")
        table.add_column("group")
        table.add_column("grade")
        table.add_column("due")
        table.add_column("submitted")
        table.add_column("graded")

        org_unit_id = self.api_helper.find_course_by_name(
            self.config.course_name
        ).org_unit.id
        dropbox_folders = {
            folder.name: folder for folder in self.api.get_dropbox_folders(org_unit_id)
        }
        group_categories = {
            category.group_category_id: category
            for category in self.api.get_group_categories(org_unit_id)
        }

        for identifier, assignment in self.config.assignments.items():
            dropbox = dropbox_folders[assignment.name]
            due_date = (
                format_datetime(to_local_time(dropbox.due_date))
                if dropbox.due_date
                else "<None>"
            )
            group_category_name = (
                group_categories[dropbox.group_type_id].name
                if dropbox.group_type_id is not None
                else "<Individual>"
            )
            grade_name = (
                self.api.get_grade_object(org_unit_id, dropbox.grade_item_id).name
                if dropbox.grade_item_id
                else "<None>"
            )
            submitted = f"{dropbox.total_users_with_submissions}/{dropbox.total_users}"
            graded = f"{dropbox.total_users_with_feedback}/{dropbox.total_users_with_submissions}"

            table.add_row(
                [
                    identifier,
                    assignment.name,
                    group_category_name,
                    grade_name,
                    due_date,
                    submitted,
                    graded,
                ]
            )

        table.print()


class ListDeadlinesCommand(APICommand):
    def __init__(self):
        super().__init__(["list", "deadlines"], "List all deadlines")

    def execute_api(self):
        table = TablePrinter()
        table.add_column("identifier")
        table.add_column("name")
        table.add_column("deadline")
        table.add_column("distributed")

        org_unit_id = self.api_helper.find_course_by_name(
            self.config.course_name
        ).org_unit.id
        dropbox_folders = {
            folder.name: folder for folder in self.api.get_dropbox_folders(org_unit_id)
        }

        for identifier, assignment in self.config.assignments.items():
            dropbox = dropbox_folders[assignment.name]
            utc_now = datetime.datetime.now(datetime.timezone.utc)

            if dropbox.due_date is None:
                deadline = "<None>"
            elif dropbox.due_date < utc_now:
                deadline = format_timedelta(utc_now - dropbox.due_date) + " ago"
            else:
                deadline = "in " + format_timedelta(dropbox.due_date - utc_now)

            distributed = (self.app.root_path / "distributions" / identifier).is_dir()
            table.add_row(
                [identifier, assignment.name, deadline, "yes" if distributed else "no"]
            )

        table.print()


class ListUngradedCommand(APICommand):
    def __init__(self):
        super().__init__(
            ["list", "ungraded"], "List all ungraded submissions for an assignment"
        )
        self.add_positional_arg(
            "assignment-id",
            "The assignment identifier",
            self.app.is_valid_assignment_id,
        )

    def execute_api(self):
        assignment_id = self.get_positional_arg(0)
        assignment_config = self.config.assignments[assignment_id]
        org_unit_id = self.api_helper.find_course_by_name(
            self.config.course_name
        ).org_unit.id
        assignment = self.api_helper.find_assignment(
            org_unit_id, assignment_config.name
        )
        submissions = self.api.get_dropbox_folder_submissions(
            org_unit_id, assignment.id
        )
        division_log = self.app.load_division_log(assignment_id)

        table = TablePrinter()
        table.add_column("name")
        table.add_column("grader")

        for submission in submissions:
            if submission.status != bsapi.types.ENTITY_DROPBOX_STATUS_SUBMITTED:
                continue

            graded_by = division_log.get_grader(submission.entity.entity_id)
            if graded_by is None:
                graded_by = "<None>"

            table.add_row([submission.entity.get_name(), graded_by])

        table.sort_rows(columns=[1])
        table.print()


class ListUndistributedCommand(APICommand):
    def __init__(self):
        super().__init__(
            ["list", "undistributed"], "List all undistributed submissions"
        )

    def execute_api(self):
        org_unit_id = self.api_helper.find_course_by_name(
            self.config.course_name
        ).org_unit.id
        assignments = {
            folder.name: folder for folder in self.api.get_dropbox_folders(org_unit_id)
        }

        table = TablePrinter()
        table.add_column("name")
        table.add_column("assignment")

        for assignment_id, assignment_config in self.config.assignments.items():
            if not self.app.has_distributed(assignment_id):
                continue

            assignment = assignments[assignment_config.name]
            submissions = self.api.get_dropbox_folder_submissions(
                org_unit_id, assignment.id
            )
            division_log = self.app.load_division_log(assignment_id)

            for submission in submissions:
                if submission.status == bsapi.types.ENTITY_DROPBOX_STATUS_UNSUBMITTED:
                    continue

                if not division_log.has_entity_id(submission.entity.entity_id):
                    table.add_row([submission.entity.get_name(), assignment.name])

        table.sort_rows(columns=[1])
        table.print()


class ListDivisionCommand(AppCommand):
    def __init__(self):
        super().__init__(
            ["list", "division"], "List the grading division made for an assignment"
        )
        self.add_positional_arg(
            "assignment-id",
            "The assignment identifier",
            self.app.is_valid_assignment_id,
        )

    def execute(self):
        assignment_id = self.get_positional_arg(0)

        table = TablePrinter()
        table.add_column("entity id")
        table.add_column("name")
        table.add_column("students")
        table.add_column("grader")

        division_log = self.app.load_division_log(assignment_id)
        for grader_id, entries in division_log:
            grader_name = self.app.config.graders[grader_id].name
            for entry in entries:
                students_str = ",".join(
                    f"{s.name} ({s.username})" for s in entry.students
                )
                table.add_row(
                    [entry.entity_id, entry.folder_name, students_str, grader_name]
                )

        table.sort_rows(columns=[3])
        table.print()
