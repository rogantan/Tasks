from app.repositories.abstract_repository import AbstractRepository
from app.models.task import Task

class TaskRepository(AbstractRepository):
  def __init__(self, session):
    super().__init__(model=Task, session=session)

