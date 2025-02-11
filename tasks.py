from storage import Storage
from utils import format_task
from models import Task

class TaskManager:
    def __init__(self):
        self.storage = Storage()
        self.tasks = self.storage.load_tasks()

    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)
        self.storage.save_tasks(self.tasks)

    def list_tasks(self, show_numbers=False):
        formatted_tasks = []
    
        if not self.tasks:
            formatted_tasks.append("No tasks available.")
            return "\n".join(formatted_tasks)
    
        for index, task in enumerate(self.tasks, 1):
            formatted_task = format_task(task, index if show_numbers else None)
            formatted_tasks.append(formatted_task)
    
        total_tasks = f"\nTotal tasks: {len(self.tasks)}"
        formatted_tasks.append(total_tasks)
    
        return "\n".join(formatted_tasks)

