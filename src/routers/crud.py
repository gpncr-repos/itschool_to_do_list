from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/tasks", tags=["tasks"])

fake_tasks = [
    {
        "id": 1,
        "title": "first_task",
        "description": "some_description",
        "done": True
    },
    {
        "id": 2,
        "title": "second_task",
        "description": "other task",
        "done": False
    }
]


@router.post("")
def create_task():
    return {"message": "task created"}


@router.get("")
def get_tasks():
    return fake_tasks


@router.put("/{task_id}")
def update_task(task_id: int, task_body: dict):
    task = None
    for i in range(len(fake_tasks)):
        if fake_tasks[i]["id"] == task_id:
            task = fake_tasks[i]

    if not task:
        raise HTTPException(status_code=404, detail="task not found")

    title = task_body["title"]
    description = task_body["description"]

    task["title"] = title
    task["description"] = description

    return task


@router.delete("/{task_id}")
def delete_task(task_id: int):
    idx = None
    for i in range(len(fake_tasks)):
        if fake_tasks[i]["id"] == task_id:
            idx = i
            break

    if idx is None:
        raise HTTPException(status_code=404, detail="task not found")

    fake_tasks.pop(idx)
