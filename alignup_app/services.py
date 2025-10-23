"""
services.py
------------
Business logic for AlignUp: handles scheduling, alignment insights,
and priority-based recommendations.

This module should never handle file I/O directly — it works with
data objects from models.py and returns structured, human-readable results.
"""

from __future__ import annotations
from datetime import datetime, timedelta
from typing import List, Optional
import random


# ---------------------------------------------------------------------------
# Core Scheduling Logic
# ---------------------------------------------------------------------------

def schedule_tasks(tasks: List) -> List[str]:
    """
    Schedule tasks in priority order and generate readable time slots.

    Args:
        tasks (List): A list of Task-like objects with `.priority` and `.name`.

    Returns:
        List[str]: Example ['09:00 AM - Review goals', '10:00 AM - Write report']
    """
    # Sort highest priority first
    tasks.sort(key=lambda t: t.priority, reverse=True)
    scheduled = []

    start_time = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
    for task in tasks:
        scheduled.append(f"{start_time.strftime('%I:%M %p')} - {task.name}")
        start_time += timedelta(hours=1)
    return scheduled


def suggest_optimal_time(task_priority: int) -> str:
    """
    Suggest the best time window for a task based on priority level.
    """
    if task_priority >= 8:
        return "🌅 Morning (9 AM – 11 AM)"
    elif task_priority >= 5:
        return "☀️ Afternoon (1 PM – 4 PM)"
    else:
        return "🌙 Evening (6 PM – 8 PM)"


# ---------------------------------------------------------------------------
# Wellness & Energy Helpers
# ---------------------------------------------------------------------------

def wellness_check() -> str:
    """
    Return a random gentle wellness reminder.
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


def suggest_task_by_energy(energy_level: str) -> str:
    """
    Suggest a suitable task type based on user-reported energy level.

    Args:
        energy_level (str): One of 'high', 'medium', or 'low'.

    Returns:
        str: Task category suggestion.
    """
    energy_level = energy_level.lower()
    if energy_level == "high":
        return "Focus-intensive work 🧠"
    elif energy_level == "medium":
        return "Collaborative or creative tasks 💬"
    elif energy_level == "low":
        return "Light organization or reflection ✍️"
    else:
        return "Rest or reset 🌿"


