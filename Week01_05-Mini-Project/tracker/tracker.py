from .task import Task
from .utils import load_tasks, save_tasks

class TaskTracker:
    def __init__(self, filepath="tasks.json"):
        self.filepath = filepath
        self.tasks = load_tasks(filepath)

    def add_task(self, task):
        self.tasks.append(task)
        self.save()

    def list_tasks(self):
        return self.tasks

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save()

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            self.save()

    def save(self):
        save_tasks(self.filepath, self.tasks)
