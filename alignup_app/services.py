from datetime import datetime, timedelta

def schedule_tasks(tasks):
    # Sort by priority descending
    tasks.sort(key=lambda t: t.priority, reverse=True)
    scheduled = []

    start_time = datetime.now().replace(hour=9, minute=0)
    for t in tasks:
        scheduled.append(f"{start_time.strftime('%I:%M %p')} - {t.name}")
        start_time += timedelta(hours=1)
    return scheduled


def suggest_optimal_time(task_priority):
    if task_priority >= 8:
        return "Morning (9 AM - 11 AM)"
    elif task_priority >= 5:
        return "Afternoon (1 PM - 4 PM)"
    else:
        return "Evening (6 PM - 8 PM)"
