"""
main.py
--------
Application entry point for AlignUp.

Coordinates all major modules:
- Creates a demo user and tasks
- Generates an aligned daily schedule
- Simulates progress and sends wellness reminders
- Produces a weekly report (placeholder)

Future versions will connect this logic to a Flask or FastAPI interface.
"""

from models import User, Task
from services import schedule_tasks, suggest_optimal_time
from utils import wellness_check
from notifications import send_notification, send_email
from progress import generate_weekly_report


def main() -> None:
    """Run the AlignUp command-line demo."""
    print("✨ Welcome to AlignUp ✨\n")

    # ------------------------------------------------------------------
    # Create a sample user and seed tasks
    # ------------------------------------------------------------------
    user = User("Natasha", email="chiedzanatasha26@gmail.com")

    sample_tasks = [
        Task("Finish project report", priority=9),
        Task("Read for 30 minutes", priority=4),
        Task("Workout", priority=6),
        Task("Journal reflection", priority=3),
    ]
    for task in sample_tasks:
        user.add_task(task)

    # ------------------------------------------------------------------
    # Generate aligned daily plan
    # ------------------------------------------------------------------
    print("📅  Your Daily Plan:")
    for slot in schedule_tasks(user.tasks):
        print(f"   • {slot}")

    # ------------------------------------------------------------------
    # Simulate progress
    # ------------------------------------------------------------------
    user.complete_task("Workout")
    user.complete_task("Finish project report")

    # ------------------------------------------------------------------
    # Provide mindful wellness reminder
    # ------------------------------------------------------------------
    print(f"\n💡 Wellness Check: {wellness_check()}")

    # ------------------------------------------------------------------
    # Notifications
    # ------------------------------------------------------------------
    send_notification("Stay focused — progress over perfection!")

    # ------------------------------------------------------------------
    # Generate & send report (placeholder)
    # ------------------------------------------------------------------
    report = generate_weekly_report(user)
    send_email(user.email, "Your AlignUp Weekly Report", report)

    print("\n✅  Session complete. Keep aligning!")


if __name__ == "__main__":
    main()
