from fastapi import APIRouter, HTTPException
from schemas.task import TaskSchema, CreateTaskSchema
from schemas.http_errors import TaskNotFondErrorSchema
from typing import List
from queries import tasks
from fastapi import Depends
from dependencies.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=TaskSchema)
async def create_task(task: CreateTaskSchema, db: AsyncSession = Depends(get_db)):
    task = await tasks.create_task(create_schema=task, db=db)
    return TaskSchema.from_orm(task)


@router.get("", response_model=List[TaskSchema])
async def get_tasks(db: AsyncSession = Depends(get_db)):
    return await tasks.get_all_tasks(db)


@router.put("/{task_id}", responses={404: {"model": TaskNotFondErrorSchema}})
async def update_task(task_id: int, task_body: CreateTaskSchema, db: AsyncSession = Depends(get_db)):
    to_update = await tasks.get_task(db, task_id)
    if to_update is None:
        raise HTTPException(status_code=404, detail="task not found")

    to_update.title = task_body.title
    to_update.done = task_body.done

    return await tasks.update_task(to_update=to_update, db=db)


@router.delete("/{task_id}", responses={404: {"model": TaskNotFondErrorSchema}})
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    to_delete = await tasks.get_task(db, task_id)
    if to_delete is None:
        raise HTTPException(status_code=404, detail="task not found")

    await tasks.delete_task(to_delete=to_delete, db=db)
