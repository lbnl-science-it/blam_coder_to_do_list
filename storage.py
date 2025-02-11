import json
from models import Task

class Storage:
    def __init__(self, filename='tasks.txt'):
        self.filename = filename

    def save_tasks(self, tasks):
        data = [{'description': t.description, 'completed': t.completed} for t in tasks]
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                if f.read().strip() == '':  # Check if file is empty
                    return []
                f.seek(0)  # Reset file pointer to beginning
                data = json.load(f)
                return [Task(t['description']) for t in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

