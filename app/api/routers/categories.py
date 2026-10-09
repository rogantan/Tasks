from fastapi import APIRouter

router = APIRouter(prefix="/categories")

@router.get("")
async def get_categories():
  pass