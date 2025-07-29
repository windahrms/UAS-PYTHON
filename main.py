from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()
DATA_FILE = "data.json"

class Task(BaseModel):
    id: int
    judul: str
    deskripsi: str

def read_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.get("/tasks")
def get_tasks():
    return read_data()

@app.post("/tasks")
def create_task(task: Task):
    data = read_data()
    data.append(task.dict())
    write_data(data)
    return {"message": "Task ditambahkan"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    data = read_data()
    for i, t in enumerate(data):
        if t["id"] == task_id:
            data[i] = task.dict()
            write_data(data)
            return {"message": "Task diperbarui"}
    raise HTTPException(status_code=404, detail="Task tidak ditemukan")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    data = read_data()
    data = [t for t in data if t["id"] != task_id]
    write_data(data)
    return {"message": "Task dihapus"}
