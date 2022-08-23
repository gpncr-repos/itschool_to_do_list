from pydantic import BaseModel, Field


class TaskSchema(BaseModel):
    id: int = Field(title="Идентификатор задачи", ge=0)
    title: str = Field(title="Описание задачи")
    done: bool = Field(False, title="Флаг выполнения задачи")

    class Config:
        orm_mode = True


class CreateTaskSchema(BaseModel):
    title: str = Field(title="Описание задачи")
    done: bool = Field(False, title="Флаг выполнения задачи")
