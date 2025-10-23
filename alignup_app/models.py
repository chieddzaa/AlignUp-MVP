"""
models.py
----------
Core data models for AlignUp.

Defines lightweight, object-oriented representations for users and tasks.
These models are designed for scalability — they can later connect
to a database ORM (e.g., SQLAlchemy) without changing the interface.
"""

from __future__ import annotations
from typing import List, Optional


class Task:
    """
    Represents a single actionable task within AlignUp.

    Attributes:
        name (str): Descriptive name of the task.
        priority (int): Priority score from 1–10. Higher = more important.
        completed (bool): Whether the task is completed.
    """

    def __init__(self, name: str, priority: int = 5, completed: bool = False) -> None:
        self.name = name
        self.priority = priority
        self.completed = completed

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def __repr__(self) -> str:
        """Readable representation for debugging and logs."""
        status = "✅" if self.completed else "⏳"
        return f"{self.name} (Priority: {self.priority}) {status}"


class User:
    """
    Represents a user within AlignUp.

    Attributes:
        name (str): User's display name.
        email (Optional[str]): Contact email.
        tasks (List[Task]): Collection of the user's tasks.
        progress_score (int): Simple numeric measure of completion progress.
    """

    def __init__(self, name: str, email: Optional[str] = None) -> None:
        self.name = name
        self.email = email
        self.tasks: List[Task] = []
        self.progress_score: int = 0  # starts at 0%

    # ---------------------------------------------------------------------
    # Task Management
    # ---------------------------------------------------------------------
    def add_task(self, task: Task) -> None:
        """Add a new Task to the user's task list."""
        self.tasks.append(task)

    def complete_task(self, task_name: str) -> bool:
        """
        Mark a task as complete by name.

        Args:
            task_name (str): The exact name of the task to complete.

        Returns:
            bool: True if the task was found and completed, False otherwise.
        """
        for t in self.tasks:
            if t.name.lower() == task_name.lower():
                if not t.completed:
                    t.mark_complete()
                    self.progress_score += 1
                return True
        return False

    def get_completed_tasks(self) -> List[Task]:
        """Return all completed tasks."""
        return [t for t in self.tasks if t.completed]

    def get_pending_tasks(self) -> List[Task]:
        """Return all tasks not yet completed."""
        return [t for t in self.tasks if not t.completed]

    def completion_rate(self) -> float:
        """Return a percentage of completed tasks."""
        total = len(self.tasks)
        if total == 0:
            return 0.0
        return (len(self.get_completed_tasks()) / total) * 100

    def __repr__(self) -> str:
        """Readable user summary."""
        return f"User({self.name}, {len(self.tasks)} tasks, {self.progress_score}% progress)"
