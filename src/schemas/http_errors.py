from pydantic import BaseModel


class TaskNotFondErrorSchema(BaseModel):
    detail: str = "Задача не найдена"
