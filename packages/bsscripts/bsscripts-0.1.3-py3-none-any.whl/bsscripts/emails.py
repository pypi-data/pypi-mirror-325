from __future__ import annotations

import email
import logging
import smtplib
from pathlib import Path
from smtplib import SMTPException
from typing import Optional

from bsscripts.config import Config, SMTPConfig
from bsscripts.division import Division
from bsscripts.download import AssignmentInfo
from bsscripts.progress import ProgressReporter

logger = logging.getLogger(__name__)


class EmailNotifier:
    def __init__(
        self,
        dist_path: Path,
        config: Config,
        smtp_config: SMTPConfig,
        assignment_info: AssignmentInfo,
        division: Division,
        progress_reporter: ProgressReporter = None,
    ):
        self.dist_path = dist_path
        self.config = config
        self.smtp_config = smtp_config
        self.assignment_info = assignment_info
        self.division = division
        self.progress_reporter = progress_reporter
        self.smtp: Optional[smtplib.SMTP] = None

    def create_notifications(self):
        distribute = self.config.distribute
        course_name = self.assignment_info.course.org_unit.name
        assignment_name = self.assignment_info.assignment.name
        assignment_id = self.assignment_info.identifier

        for grader_id, submissions in self.division:
            grader_info = self.config.graders[grader_id]
            num_submissions = len(submissions)

            # Create target file path, and ensure parent folders exists.
            parent_path = self.dist_path.resolve() / assignment_id
            archive_path = parent_path / f"{assignment_id}-{grader_id}.7z"
            message_path = parent_path / f"{assignment_id}-{grader_id}.message"
            password_path = parent_path / f"{assignment_id}-{grader_id}.password"
            parent_path.mkdir(parents=True, exist_ok=True)

            password = (
                password_path.read_text(encoding="utf-8")
                if password_path.exists()
                else None
            )

            with open(message_path, "w", encoding="utf-8") as f:
                f.write(
                    f'You have {num_submissions} submission{"s" if num_submissions != 1 else ""} to grade for {course_name} - {assignment_name}.\n'
                )
                f.write("\n")
                if num_submissions == 0:
                    f.write(
                        "As you have nothing to grade, no submissions archive was created.\n"
                    )
                else:
                    f.write(f"password: {password}\n")
                    # TODO: This is specific to SCP uploads.
                    # If we end up supporting different modes then perhaps an Uploader instance has to generate the text below?
                    f.write("\n")
                    f.write("Grab your submissions using the following command:\n")
                    f.write(
                        f"    scp {grader_info.distribute_username}@{distribute.host}:{distribute.share}/{assignment_id}/{archive_path.name} ./\n"
                    )
                    f.write("Then extract it using the following command:\n")
                    f.write(
                        f"    7za x -o{assignment_id} -p{password} {archive_path.name} > /dev/null\n"
                    )

    def initialize(self) -> bool:
        try:
            self.smtp = smtplib.SMTP(self.smtp_config.host, self.smtp_config.port)
            self.smtp.starttls()
            self.smtp.login(self.smtp_config.username, self.smtp_config.password)
            return True
        except smtplib.SMTPException as e:
            self.smtp = None
            logger.fatal(
                "SMTP exception during connection establishment: %s", type(e).__name__
            )
            return False

    def _send_mail(self, subject: str, content: str, to: str):
        msg = email.message.EmailMessage()
        msg["Subject"] = subject
        msg["From"] = self.smtp_config.from_
        msg["To"] = to
        msg.set_content(content)

        try:
            self.smtp.send_message(msg)
        except smtplib.SMTPException as e:
            logger.error(
                "SMTP exception while sending email to %s: %s", to, type(e).__name__
            )

    def send_notifications(self):
        assert self.smtp is not None, "SMTP client not initialized correctly"

        course_name = self.assignment_info.course.org_unit.name
        assignment_name = self.assignment_info.assignment.name
        assignment_id = self.assignment_info.identifier
        subject = f"{course_name}: {assignment_name}"
        graders = len(self.division.graders())

        for idx, grader_id in enumerate(self.division.graders()):
            if self.progress_reporter:
                self.progress_reporter.start(idx + 1, graders, grader_id)

            mail_to = self.config.graders[grader_id].distribute_email
            message_path = (
                self.dist_path / assignment_id / f"{assignment_id}-{grader_id}.message"
            )
            message_contents = message_path.read_text(encoding="utf-8")

            self._send_mail(subject, message_contents, mail_to)

        if self.progress_reporter:
            self.progress_reporter.finish(graders)

    def shutdown(self):
        if self.smtp is not None:
            try:
                self.smtp.quit()
            except (OSError, SMTPException):
                pass
            self.smtp = None
