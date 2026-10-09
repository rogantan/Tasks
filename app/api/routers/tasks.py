from fastapi import APIRouter
from schemas.tasks import TaskCreate,TaskRead, TaskUpdate

router = APIRouter(prefix="/tasks")

@router.get("")
async def get_tasks():
  pass

@router.post("")
async def create_task():
  pass

@router.put("")
async def update_task():
  pass

@router.delete("")
async def delete_task():
  pass