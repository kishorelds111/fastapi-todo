import json
import os

class TodoApp:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        return self.tasks

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            deleted = self.tasks.pop(index)
            self.save_tasks()
            return deleted
        return None
