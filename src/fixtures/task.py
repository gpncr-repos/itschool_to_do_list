import factory
from models import task
from factory_boy_extra.async_sqlalchemy_factory import AsyncSQLAlchemyModelFactory


class TaskFactory(AsyncSQLAlchemyModelFactory):
    class Meta:
        model = task.Task

    id = factory.Sequence(lambda n: n)
    title = factory.Sequence(lambda n: 'Some Task %d' % n)
    done = factory.Faker("pybool")
