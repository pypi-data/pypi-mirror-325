import email
import logging
import smtplib

from bsscripts.commands import AppCommand

logger = logging.getLogger(__name__)


class ResendNotificationsCommand(AppCommand):
    def __init__(self):
        super().__init__(
            ["resend", "notifications"], "Resend email notifications for an assignment"
        )
        self.add_positional_arg(
            "assignment-id",
            "The assignment identifier",
            self.app.is_valid_assignment_id,
        )
        self.smtp = None

    def _send_mail(self, subject: str, content: str, to: str):
        msg = email.message.EmailMessage()
        msg["Subject"] = subject
        msg["From"] = self.app.smtp_config.from_
        msg["To"] = to
        msg.set_content(content)

        try:
            self.smtp.send_message(msg)
        except smtplib.SMTPException as e:
            logger.error(
                "SMTP exception while sending email to %s: %s", to, type(e).__name__
            )

    def execute(self):
        # TODO: Perhaps tie it in to the Notifier itself?
        # At least extract some duplicated email setup/sending code into a utils.SMTPMailer class or something?
        assignment_id = self.get_positional_arg(0)
        if not self.app.has_distributed(assignment_id):
            logger.error("Assignment has not yet been distributed")
            return

        course_name = self.app.config.course_name
        assignment_name = self.app.config.assignments[assignment_id].name
        subject = f"{course_name}: {assignment_name}"

        try:
            self.smtp = smtplib.SMTP(
                self.app.smtp_config.host, self.app.smtp_config.port
            )
            self.smtp.starttls()
            self.smtp.login(
                self.app.smtp_config.username, self.app.smtp_config.password
            )
        except smtplib.SMTPException as e:
            logger.fatal(
                "SMTP exception during connection establishment: %s", type(e).__name__
            )
            return

        distribution_path = self.app.root_path / "distributions" / assignment_id
        for message_path in distribution_path.iterdir():
            if not message_path.is_file():
                continue
            if not message_path.suffix == ".message":
                continue

            grader_id = message_path.stem.removeprefix(f"{assignment_id}-")
            grader_mail = self.app.config.graders[grader_id].distribute_email
            message_contents = message_path.read_text(encoding="utf-8")

            print(f"Resending {grader_id} to {grader_mail}")
            self._send_mail(subject, message_contents, grader_mail)

        self.smtp.quit()
