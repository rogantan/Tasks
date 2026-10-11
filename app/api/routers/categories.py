from fastapi import APIRouter

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("")
async def get_categories():
  pass

@router.get("/{category_id}")
async def get_category():
  pass

@router.post("")
async def create_category():
  pass

@router.put("")
async def update_category():
  pass

@router.delete("")
async def delete_category():
  pass