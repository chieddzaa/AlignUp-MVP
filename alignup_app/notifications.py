"""
notifications.py
-----------------
Handles user notifications for AlignUp.

Right now, it provides console-based reminders and mock email sending.
Later, this will integrate with real services like SendGrid, Gmail API,
or Twilio for multi-channel notifications.
"""

from __future__ import annotations
from typing import Optional
from alignup_app import logger


# ----------------------------------------------------------------------
# Core Notification Logic
# ----------------------------------------------------------------------

def send_notification(message: str, recipient: Optional[str] = None) -> None:
    """
    Send a quick notification (console-based for MVP).

    Args:
        message (str): The message to send.
        recipient (Optional[str]): Recipient name or email (optional).
    """
    if recipient:
        logger.info(f"Notification sent to {recipient}: {message}")
        print(f"🔔  [Notify {recipient}] {message}")
    else:
        logger.info(f"Notification: {message}")
        print(f"🔔  {message}")


def send_email(to_email: str, subject: str, body: str) -> None:
    """
    Simulate sending an email.

    Args:
        to_email (str): Recipient email address.
        subject (str): Subject line.
        body (str): Email content (text or HTML).
    """
    logger.info(f"Email sent to {to_email} | Subject: {subject}")
    print("\n📧  --- Email Simulation ---")
    print(f"To: {to_email}")
    print(f"Subject: {subject}")
    print(f"Body:\n{body}")
    print("📨  -------------------------")


def send_daily_reminder(user_name: str) -> None:
    """
    Example of a specialized notification for daily check-ins.
    """
    message = f"Hey {user_name}, remember to review your goals and breathe 🌿"
    send_notification(message, recipient=user_name)
