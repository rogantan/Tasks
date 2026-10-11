from fastapi import APIRouter
from app.api.routers.tasks import router as r1
from app.api.routers.categories import router as r2

router = APIRouter(prefix="/v1")

router.include_router(r1)
router.include_router(r2)