class Task:
    def __init__(self, name, priority=5, completed=False):
        self.name = name
        self.priority = priority
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def __repr__(self):
        status = "✅" if self.completed else "⏳"
        return f"{self.name} (Priority: {self.priority}) {status}"


class User:
    def __init__(self, name, email=None):
        self.name = name
        self.email = email
        self.tasks = []
        self.progress_score = 0  # starts at 0%

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task_name):
        for t in self.tasks:
            if t.name == task_name:
                t.mark_complete()
                self.progress_score += 1  # each completion = +1%
