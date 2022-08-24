import pytest
from queries import tasks
from fixtures.task import TaskFactory
from schemas.task import CreateTaskSchema


@pytest.mark.asyncio
async def test_get_tasks(sa_session):
    task = TaskFactory.build()
    sa_session.add(task)
    sa_session.flush()

    all_tasks = await tasks.get_all_tasks(sa_session)
    assert all_tasks
    assert len(all_tasks) == 1
    assert all_tasks[0] == task


@pytest.mark.asyncio
async def test_get_task(sa_session):
    task = TaskFactory.build()
    sa_session.add(task)
    sa_session.flush()

    current_task = await tasks.get_task(sa_session, task.id)
    assert current_task is not None
    assert current_task.id == task.id


@pytest.mark.asyncio
async def test_update_task(sa_session):
    task = TaskFactory.build()
    sa_session.add(task)
    sa_session.flush()

    task.title = "updated"

    current_task = await tasks.update_task(sa_session, to_update=task)
    assert current_task is not None
    assert current_task.id == task.id
    assert current_task.title == "updated"


@pytest.mark.asyncio
async def test_create_task(sa_session):
    task = CreateTaskSchema(title="test")

    current_task = await tasks.create_task(sa_session, create_schema=task)
    assert current_task is not None
    assert current_task.title == "test"


@pytest.mark.asyncio
async def test_delete_task(sa_session):
    task = TaskFactory.build()
    sa_session.add(task)
    sa_session.flush()

    result = await tasks.delete_task(sa_session, to_delete=task)
    assert result is None
    assert not sa_session.new
    assert not sa_session.dirty
    assert not sa_session.deleted
