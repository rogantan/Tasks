from fastapi import APIRouter, Depends
from app.schemas.tasks import TaskCreate,TaskRead, TaskUpdate
from app.services.task import TaskService
from app.api.dependencies import get_task_service
from typing import List

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("", response_model=List[TaskRead])
async def get_tasks(task_service: TaskService = Depends(get_task_service)) -> List[TaskRead]:
  return await task_service.list_tasks()

@router.get("/{task_id}", response_model=TaskRead)
async def get_task(task_id: int, task_service: TaskService = Depends(get_task_service)) -> TaskRead:
  return await task_service.get_task(task_id)

@router.post("")
async def create_task(payload: TaskCreate, task_service: TaskService = Depends(get_task_service)):
  return await task_service.create_task(payload)

@router.put("")
async def update_task(task_id: int, payload: TaskUpdate, task_service: TaskService = Depends(get_task_service)):
  return await task_service.update_task(task_id, payload)

@router.delete("")
async def delete_task(task_id: int, task_service: TaskService = Depends(get_task_service)):
  return await task_service.delete_task(task_id)