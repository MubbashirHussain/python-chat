from fastapi import APIRouter
from pydantic import BaseModel
from app.controllers.auth import registerController, loginController


router = APIRouter(tags=["auth"])


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
