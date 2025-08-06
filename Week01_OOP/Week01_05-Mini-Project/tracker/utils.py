import json
import time
from .task import Task

def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"⏱️  {func.__name__} took {time.time() - start:.2f} seconds")
        return result
    return wrapper

def load_tasks(filepath): 
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return [Task.from_dict(t) for t in data]
    except FileNotFoundError:
        return []

def save_tasks(filepath, tasks):
    with open(filepath, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)
    