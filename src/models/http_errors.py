from pydantic import BaseModel


class TaskNotFondError(BaseModel):
    detail: str = "Задача не найдена"
