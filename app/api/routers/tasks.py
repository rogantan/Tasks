from fastapi import APIRouter
from app.schemas.tasks import TaskCreate,TaskRead, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["Tasks"])

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