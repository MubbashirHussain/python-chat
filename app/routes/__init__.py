from fastapi import APIRouter
from app.routes.auth import router as auth_router
from app.routes.user import router as user_router


router = APIRouter(prefix="/api")
router.include_router(auth_router, prefix="/auth")
router.include_router(user_router, prefix="/user")
