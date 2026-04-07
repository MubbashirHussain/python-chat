from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from app.utils.security import (
    get_password_hash,
    verify_password,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from app.config.database import user_collection
from app.models.user import UserModel
from datetime import timedelta, datetime, timezone
from app.utils.responses import res_created, res_success_data, res_bad_request

from app.controllers.user import registerController, loginController


router = APIRouter(prefix="/api/auth", tags=["auth"])


class UserRegisterRequest(BaseModel):
    username: str
    password: str
    profilePicture: str | None = None
    bio: str | None = None


class UserLoginRequest(BaseModel):
    username: str
    password: str


@router.post("/register")
async def Register(user: UserRegisterRequest):
    return await registerController(user)


@router.post("/login")
async def Login(user: UserLoginRequest):
    return await loginController(user)
