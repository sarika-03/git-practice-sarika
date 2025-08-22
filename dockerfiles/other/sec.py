import os
import json
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# ---------------- Config ----------------
DATA_FILE = os.getenv("DATA_FILE", "/data/tasks.json")

os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# ---------------- Models ----------------
class Task(BaseModel):
    id: int
    title: str
    done: bool = False

# ---------------- Helpers ----------------
def load_tasks() -> List[dict]:
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks: List[dict]) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# ---------------- FastAPI App ----------------
app = FastAPI(title="Task Manager API")

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return load_tasks()

@app.post("/tasks", response_model=Task)
def add_task(task: Task):
    tasks = load_tasks()
    if any(t["id"] == task.id for t in tasks):
        raise HTTPException(status_code=400, detail="Task ID already exists")
    tasks.append(task.dict())
    save_tasks(tasks)
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    save_tasks(new_tasks)
    return {"deleted": task_id}

@app.get("/health")
def health():
    return {"status": "ok"}
