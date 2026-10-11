from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schemas.tasks import TaskRead, TaskUpdate, TaskCreate
from app.repositories.task_repository import TaskRepository

class TaskService:

  def __init__(self, session: AsyncSession):
    self.session = session
    self.repository = TaskRepository(self.session)
    
  async def list_tasks(self) -> List[TaskRead]:
    tasks_result = await self.repository.get_all()
    return [TaskRead.model_validate(task) for task in tasks_result]

  async def get_task(self, task_id: int) -> TaskRead:
    task = await self.repository.get_by_id(task_id)
    return TaskRead.model_validate(task)

  async def create_task(self, payload: TaskCreate):
    data = payload.model_dump()
    task_new = await self.repository.insert(**data)
    await self.session.commit()
    return TaskRead.model_validate(task_new)

  async def update_task(self, task_id: int, payload: TaskUpdate):
    data = {}
    if payload.title is not None:
      data["title"] = payload.title
    if payload.completed is not None:
      data["completed"] = payload.completed
    task_updated = await self.repository.update(task_id, **data)
    await self.session.commit()
    if task_updated:
      return TaskRead.model_validate(task_updated)

  async def delete_task(self, task_id: int):
    await self.repository.delete(task_id)
    await self.session.commit()