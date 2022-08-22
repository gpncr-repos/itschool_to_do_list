from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int = Field(title="Идентификатор задачи", ge=0)
    title: str = Field(title="Описание задачи")
    done: bool = Field(False, title="Флаг выполнения задачи")


class CreateTask(BaseModel):
    title: str = Field(title="Описание задачи")
    done: bool = Field(False, title="Флаг выполнения задачи")
