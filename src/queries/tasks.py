from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import task
from schemas.task import CreateTaskSchema


async def create_task(db: AsyncSession, create_schema: CreateTaskSchema):
    model = task.Task(**create_schema.dict())
    db.add(model)
    await db.commit()
    await db.refresh(model)
    return model


async def get_all_tasks(db: AsyncSession):
    stmt = select(task.Task)
    result = await db.execute(stmt)
    return result.scalars().all()


async def update_task(db: AsyncSession, to_update: task.Task):
    db.add(to_update)
    await db.commit()
    await db.refresh(to_update)
    return to_update


async def delete_task(db: AsyncSession, to_delete: task.Task):
    await db.delete(to_delete)
    await db.commit()


async def get_task(db: AsyncSession, task_id: int):
    stmt = select(task.Task).where(task.Task.id == task_id).limit(1)
    result = await db.execute(stmt)
    return result.scalars().first()
