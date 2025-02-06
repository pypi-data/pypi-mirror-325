import logging
from dataclasses import dataclass

import bsapi
import bsapi.helper
import bsapi.types

from bsscripts.commands import APICommand, AppCommand
from bsscripts.utils import TablePrinter, is_match

logger = logging.getLogger(__name__)


class CheckGradingProgressCommand(APICommand):
    @dataclass
    class Progress:
        draft: int
        published: int
        assigned: int

    def __init__(self):
        super().__init__(
            ["check", "grading", "progress"],
            "Check the grading progress of an assignment",
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
        table.add_column("grader")
        table.add_column("draft")
        table.add_column("published")
        table.add_column("assigned")
        table.add_column("completed")

        progress = {
            grader: CheckGradingProgressCommand.Progress(0, 0, 0)
            for grader in self.config.graders
        }

        for submission in submissions:
            if submission.status == bsapi.types.ENTITY_DROPBOX_STATUS_UNSUBMITTED:
                continue
            if not division_log.has_entity_id(submission.entity.entity_id):
                continue

            graded_by = division_log.get_grader(submission.entity.entity_id)
            progress[graded_by].assigned += 1

            if submission.status == bsapi.types.ENTITY_DROPBOX_STATUS_PUBLISHED:
                progress[graded_by].published += 1
            elif submission.status == bsapi.types.ENTITY_DROPBOX_STATUS_DRAFT:
                progress[graded_by].draft += 1

        for grader_id, progress in progress.items():
            if progress.assigned == 0:
                continue

            if progress.published == progress.assigned:
                completed = "yes"
            elif progress.draft + progress.published == progress.assigned:
                completed = "draft"
            else:
                completed = "no"

            table.add_row(
                [
                    self.config.graders[grader_id].name,
                    progress.draft,
                    progress.published,
                    progress.assigned,
                    completed,
                ]
            )

        table.sort_rows()
        table.print()


class FindGraderCommand(AppCommand):
    def __init__(self):
        super().__init__(["find", "grader"], "Find the grader for a search term")
        self.add_positional_arg("search", "The search term")

    def execute(self):
        search = self.get_positional_arg(0)

        table = TablePrinter()
        table.add_column("entity id")
        table.add_column("name")
        table.add_column("students")
        table.add_column("grader")
        table.add_column("assignment")

        for assignment_id, assignment in self.app.config.assignments.items():
            if not self.app.has_distributed(assignment_id):
                continue

            division_log = self.app.load_division_log(assignment_id)
            for grader_id, entries in division_log:
                grader_name = self.app.config.graders[grader_id].name
                for entry in entries:
                    students_str = ",".join(
                        f"{s.name} ({s.username})" for s in entry.students
                    )

                    if is_match(search, entry.folder_name) or is_match(
                        search, students_str
                    ):
                        table.add_row(
                            [
                                entry.entity_id,
                                entry.folder_name,
                                students_str,
                                grader_name,
                                assignment.name,
                            ]
                        )

        table.sort_rows(columns=[4])
        table.print()


class CheckGradingGroupsCommand(APICommand):
    def __init__(self):
        super().__init__(
            ["check", "grading", "groups"], "Check the grading groups of an assignment"
        )
        self.add_positional_arg(
            "assignment-id",
            "The assignment identifier",
            self.app.is_valid_assignment_id,
        )

    def execute_api(self):
        assignment_id = self.get_positional_arg(0)
        assignment_config = self.config.assignments[assignment_id]

        if assignment_config.division.method != "brightspace":
            return

        # Grab all required Brightspace metadata once to avoid making further API calls.
        org_unit_id = self.api_helper.find_course_by_name(
            self.config.course_name
        ).org_unit.id
        grading_group_category = self.api_helper.find_group_category(
            org_unit_id, assignment_config.division.group_category_name
        )
        assignment = self.api_helper.find_assignment(
            org_unit_id, assignment_config.name
        )
        users = {
            int(user.user.identifier): user.user
            for user in self.api.get_users(org_unit_id)
        }
        groups = (
            {
                group.group_id: group
                for group in self.api.get_groups(org_unit_id, assignment.group_type_id)
            }
            if assignment.group_type_id is not None
            else None
        )
        grading_groups = {
            group.group_id: group
            for group in self.api.get_groups(
                org_unit_id, grading_group_category.group_category_id
            )
        }

        # Build a map of user identifier to a list of grading groups they are enrolled in, if any.
        user_to_grading_groups: dict[int, list[int]] = {
            user_id: [] for user_id in users
        }
        for grading_group in grading_groups.values():
            for user_id in grading_group.enrollments:
                user_to_grading_groups[user_id].append(grading_group.group_id)

        # If this is a group assignment, build a map of user identifier to assignment group.
        user_to_group: dict[int, int] = dict()
        if groups is not None:
            for group in groups.values():
                for user_id in group.enrollments:
                    user_to_group[user_id] = group.group_id

        # Loop over all users, and check if they are in exactly one grading group.
        for user_id, in_grading_groups in user_to_grading_groups.items():
            if len(in_grading_groups) == 1:
                continue

            user = users[user_id]

            # User is either not in any grading groups, or in multiple, so show this.
            if len(in_grading_groups) == 0:
                print(
                    f"{user.display_name} ({user.user_name.lower()}) is not in any grading group"
                )
            elif len(in_grading_groups) > 1:
                groups_str = ", ".join(
                    grading_groups[group_id].name for group_id in in_grading_groups
                )
                print(
                    f"{user.display_name} ({user.user_name.lower()}) is in multiple grading groups: {groups_str}"
                )

            # Check if we have a group assignment, and whether the user is in an assignment group.
            if user_id not in user_to_group:
                continue

            # We have a group assignment, and the user is part of a group, so show which one.
            group = groups[user_to_group[user_id]]
            print(f"- In assignment group {group.name}")

            # Also show information on any group partners, such as their grading group membership.
            for partner_id in group.enrollments:
                if partner_id == user_id:
                    continue

                partner = users[partner_id]
                partner_grading_groups = user_to_grading_groups[partner_id]
                print(
                    f"- Group partner {partner.display_name} ({partner.user_name.lower()}) ",
                    end="",
                )
                if partner_grading_groups:
                    groups_str = ", ".join(
                        grading_groups[group_id].name
                        for group_id in partner_grading_groups
                    )
                    print(f"is in grading group(s): {groups_str}")
                else:
                    print("is not in any grading group")

        # Finally, loop over all assignment groups and check whether there are any split groups.
        # A split group is one that has more than one member, and not all members are part of the same grading group(s).
        for group in groups.values():
            if len(group.enrollments) <= 1:
                continue
            if all(
                user_to_grading_groups[group.enrollments[0]]
                == user_to_grading_groups[user_id]
                for user_id in group.enrollments
            ):
                continue

            print(f"Group {group.name} is split over multiple grading groups")
            for user_id in group.enrollments:
                user = users[user_id]
                print(
                    f"- Group member {user.display_name} ({user.user_name.lower()}) ",
                    end="",
                )

                in_grading_groups = user_to_grading_groups[user_id]
                if in_grading_groups:
                    groups_str = ", ".join(
                        grading_groups[group_id].name for group_id in in_grading_groups
                    )
                    print(f"is in grading group(s): {groups_str}")
                else:
                    print("is not in any grading group")
