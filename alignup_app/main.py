from models import User, Task
from services import schedule_tasks, suggest_optimal_time
from utils import wellness_check
from notifications import send_notification, send_email
from progress import generate_weekly_report

def main():
    print("✨ Welcome to AlignUp ✨")

    user = User("Natasha", email="chiedzanatasha26@gmail.com")

    # Add sample tasks
    tasks = [
        Task("Finish project report", priority=9),
        Task("Read for 30 minutes", priority=4),
        Task("Workout", priority=6),
        Task("Journal reflection", priority=3),
    ]
    for t in tasks:
        user.add_task(t)

    # Schedule tasks
    scheduled = schedule_tasks(user.tasks)
    print("\n📅 Your Daily Plan:")
    for s in scheduled:
        print(f"- {s}")

    # Simulate completing tasks
    user.complete_task("Workout")
    user.complete_task("Finish project report")

    # Wellness reminder
    print("\n💡 Wellness Check:", wellness_check())

    # Notification example
    send_notification("Stay focused — progress over perfection!")

    # Generate & send report
    report = generate_weekly_report(user)
    send_email(user.email, "Your AlignUp Weekly Report", report)

if __name__ == "__main__":
    main()
