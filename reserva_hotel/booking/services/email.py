from django.core.mail import send_mail
from django.conf import settings


class EmailService:
    @staticmethod
    def send_email(
        subject: str,
        message: str,
        recipient_list: list,
    ):
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST,
            recipient_list
        )