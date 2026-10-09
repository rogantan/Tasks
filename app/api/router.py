from fastapi import APIRouter
from app.api.routers.tasks import router as r1

router = APIRouter(prefix="/v1")

router.include_router(r1)