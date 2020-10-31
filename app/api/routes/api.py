from fastapi import APIRouter

from app.api.routes import account

router = APIRouter()

router.include_router(account.router, tags=[""], prefix="/v1")