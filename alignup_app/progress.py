"""
progress.py
------------
Handles progress tracking, analytics, and report generation for AlignUp.

Right now, this module produces a simple weekly report using the
user's task data. In later versions, it will integrate with analytics
and journaling features for personalized insights.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime
from alignup_app import logger

if TYPE_CHECKING:
    from alignup_app.models import User


# ----------------------------------------------------------------------
# Core Progress Functions
# ----------------------------------------------------------------------

def calculate_completion_rate(user: "User") -> float:
    """
    Calculate the user's task completion rate as a percentage.

    Args:
        user (User): The user whose progress is being measured.

    Returns:
        float: Completion percentage (0–100).
    """
    total = len(user.tasks)
    if total == 0:
        return 0.0
    completed = len([t for t in user.tasks if t.completed])
    rate = (completed / total) * 100
    logger.info(f"Calculated completion rate for {user.name}: {rate:.1f}%")
    return rate


def generate_weekly_report(user: "User") -> str:
    """
    Generate a text-based weekly progress report for the user.

    Args:
        user (User): The user to report on.

    Returns:
        str: A formatted report string.
    """
    completion = calculate_completion_rate(user)
    completed = [t.name for t in user.tasks if t.completed]
    pending = [t.name for t in user.tasks if not t.completed]

    report = [
        f"🗓️  AlignUp Weekly Report — {datetime.now().strftime('%Y-%m-%d')}",
        f"👤  User: {user.name}",
        "",
        f"✅  Completed Tasks ({len(completed)}):",
    ]
    report.extend([f"   • {name}" for name in completed] or ["   • None yet"])

    report.append("")
    report.append(f"⏳  Pending Tasks ({len(pending)}):")
    report.extend([f"   • {name}" for name in pending] or ["   • None 🎉"])

    report.append("")
    report.append(f"📈  Completion Rate: {completion:.1f}%")
    report.append("🌿  Remember: progress is built in rhythm, not rush.")
    report.append("----------------------------------------------------")

    logger.info(f"Generated weekly report for {user.name}")
    return "\n".join(report)
