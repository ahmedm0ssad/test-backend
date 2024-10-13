tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Build an API", "completed": False},
]

def get_all_tasks():
    return tasks

def get_task_by_id(task_id):
    return next((task for task in tasks if task["id"] == task_id), None)

def create_task(title):
    new_task = {"id": len(tasks) + 1, "title": title, "completed": False}
    tasks.append(new_task)
    return new_task

def update_task(task_id, title, completed):
    task = get_task_by_id(task_id)
    if task:
        if title is not None:
            task['title'] = title
        if completed is not None:
            task['completed'] = completed
        return task
    return None

def delete_task(task_id):
    task = get_task_by_id(task_id)
    if task:
        tasks.remove(task)
        return True
    return False
