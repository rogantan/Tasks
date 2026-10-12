from app.services.task import TaskService
from app.repositories.task_repository import TaskRepository
from fastapi import Depends
from app.db.db_postgres import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings


def get_task_service(session: AsyncSession = Depends(get_session)):
  return TaskService(session, settings.get_redis_url, settings.CACHE_TTL_SECONDS, settings.CACHE_KEY_TASKS)