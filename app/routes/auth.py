from fastapi import APIRouter, UploadFile, File, Form
from pydantic import BaseModel
from app.controllers.auth import registerController, loginController


router = APIRouter(tags=["auth"])


class UserLoginRequest(BaseModel):
    username: str
    password: str


@router.post("/register")
async def Register(
    username: str = Form(...),
    password: str = Form(...),
    name: str = Form(...),
    email: str = Form(...),
    bio: str = Form(...),
    profilePicture: UploadFile = File(...),
):
    return await registerController(
        {
            "username": username,
            "password": password,
            "name": name,
            "email": email,
            "bio": bio,
            "profilePicture": profilePicture,
        }
    )


@router.post("/login")
async def Login(user: UserLoginRequest):
    return await loginController(user)
