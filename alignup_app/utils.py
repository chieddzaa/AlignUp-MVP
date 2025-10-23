"""
Utility functions for AlignUp — general-purpose helpers that support 
user wellness, formatting, and lightweight logic used across modules.
"""

import random
from datetime import datetime


def wellness_check() -> str:
    """
    Return a random gentle wellness reminder.

    Examples:
        >>> wellness_check()
        'Drink some water 💧'

    Returns:
        str: A simple self-care prompt.
    """
    checks = [
        "Take a deep breath 🌿",
        "Stretch for 2 minutes 💪",
        "Drink some water 💧",
        "Step away from your screen 👀",
        "Reflect on one thing you’re grateful for 🙏",
        "Smile — progress is still progress 🙂",
    ]
    return random.choice(checks)


def current_time() -> str:
    """
    Return the current time formatted for journaling or notifications.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

