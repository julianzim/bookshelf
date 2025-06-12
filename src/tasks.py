import smtplib
from email.message import EmailMessage
from typing import Literal

from src.celery_app import app
from src.config import email_config
from misc.utils import get_logger


logger = get_logger(name=__name__)

MessageType = Literal['plain', 'html']


@app.task(name="send_email", queue="email")
def send_email(
    subject: str,
    body: str,
    recipients: list[str],
    subtype: MessageType = "html"
):
    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = email_config.MAIL_FROM
    message['To'] = ', '.join(recipients)
    message.set_content(body, subtype)

    try:
        with smtplib.SMTP(email_config.MAIL_SERVER, email_config.MAIL_PORT) as smtp:
            smtp.starttls()
            smtp.login(email_config.MAIL_USERNAME, email_config.MAIL_PASSWORD)
            smtp.send_message(message)
        logger.info("Email sent successfully. From: %s, To: %s", email_config.MAIL_FROM, recipients)
    except Exception as e:
        logger.error("Failed to send email: %s", e)
        raise
