from fastapi import APIRouter, HTTPException
from models.task import Task, CreateTask
from models.http_errors import TaskNotFondError
from typing import List

router = APIRouter(prefix="/tasks", tags=["tasks"])

fake_tasks = [
    Task(**{
        "id": 1,
        "title": "first_task",
        "done": True
    }),
    Task(**{
        "id": 2,
        "title": "second_task",
        "description": "other task",
        "done": False
    })
]


@router.post("", response_model=Task)
def create_task(task: CreateTask):
    sorted_tasks = sorted(fake_tasks, key=lambda task: task.id, reverse=True)
    if sorted_tasks:
        last_task_id = sorted_tasks[0].id
        last_task_id += 1
    else:
        last_task_id = 1

    to_add = Task(id=last_task_id, title=task.title)
    fake_tasks.append(to_add)

    return to_add


@router.get("", response_model=List[Task])
def get_tasks():
    return fake_tasks


@router.put("/{task_id}", responses={404: {"model": TaskNotFondError}})
def update_task(task_id: int, task_body: CreateTask):
    task = None
    for i in range(len(fake_tasks)):
        if fake_tasks[i].id == task_id:
            task = fake_tasks[i]

    if not task:
        raise HTTPException(status_code=404, detail="task not found")

    title = task_body.title
    task.title = title

    return task


@router.delete("/{task_id}", responses={404: {"model": TaskNotFondError}})
def delete_task(task_id: int):
    idx = None
    for i in range(len(fake_tasks)):
        if fake_tasks[i].id == task_id:
            idx = i
            break

    if idx is None:
        raise HTTPException(status_code=404, detail="task not found")

    fake_tasks.pop(idx)
