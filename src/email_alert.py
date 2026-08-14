import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv


load_dotenv()


def create_email_alert(summary):
    """
    Create the subject and body of the email alert.
    """

    subject = "AI Anomaly Agent - Business Alert"

    body = f"""
Hello,

The AI Anomaly Agent detected unusual changes in your business data.

ANOMALY SUMMARY
---------------

{summary}

Please review the affected metrics and investigate the possible cause.

This is an automated alert from the AI Anomaly Agent.
"""

    return subject, body


def send_email(subject, body):
    """
    Send an email alert using Gmail SMTP.
    """

    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")

    if not sender_email:
        raise ValueError("SENDER_EMAIL is missing from .env")

    if not sender_password:
        raise ValueError("SENDER_PASSWORD is missing from .env")

    if not receiver_email:
        raise ValueError("RECEIVER_EMAIL is missing from .env")

    message = EmailMessage()

    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.set_content(body)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)

    print("Email sent successfully!")