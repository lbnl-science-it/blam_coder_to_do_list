def format_task(task, task_number=None):
    status = '✓' if task.completed else '✗'
    if task_number is not None:
        return f"{task_number:2d}. [{status}] {task.description}"
    return f"[{status}] {task.description}"

