from db_settings import Base
import sqlalchemy as sa


class Task(Base):
    __tablename__ = "tasks"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, comment="Идентификатор задачи")
    title = sa.Column(sa.String, nullable=False, comment="Описание задачи")
    done = sa.Column(sa.Boolean, nullable=False, comment="Флаг выполнения задачи")
