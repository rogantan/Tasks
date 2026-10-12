from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schemas.tasks import TaskRead, TaskUpdate, TaskCreate
from app.repositories.task_repository import TaskRepository
from app.cache.redis import RedisCache

class TaskService:

  def __init__(
    self, 
    session: AsyncSession, 
    redis_url: str, 
    cache_ttl_seconds: int,
    cache_tasks_key: str
  ):
    self.session = session
    self.repository = TaskRepository(self.session)
    self.redis = RedisCache(redis_url, cache_ttl_seconds)
    self.cache_tasks_key = cache_tasks_key
    
  async def list_tasks(self) -> List[TaskRead]:
    cached_tasks = await self.redis.get(self.cache_tasks_key)
    if cached_tasks:
      return cached_tasks

    tasks_result = await self.repository.get_all()
    tasks = [TaskRead.model_validate(task) for task in tasks_result]

    cached_tasks = [task.model_dump() for task in tasks]
    await self.redis.set(self.cache_tasks_key, cached_tasks)

    return tasks

  async def get_task(self, task_id: int) -> TaskRead:
    task = await self.repository.get_by_id(task_id)
    if task:
      return TaskRead.model_validate(task)

  async def create_task(self, payload: TaskCreate):
    await self.redis.delete(self.cache_tasks_key)
    data = payload.model_dump()
    task_new = await self.repository.insert(**data)
    await self.session.commit()
    return TaskRead.model_validate(task_new)

  async def update_task(self, task_id: int, payload: TaskUpdate):
    await self.redis.delete(self.cache_tasks_key)
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
    await self.redis.delete(self.cache_tasks_key)
    await self.repository.delete(task_id)
    await self.session.commit()