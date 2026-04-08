from fastapi import APIRouter, Depends, File, Form, UploadFile
from pydantic import BaseModel
import app.controllers.user as UserController
from app.middlewares.auth import verifyToken
from typing import Optional

router = APIRouter(tags=["user"])


class updateMeBody(BaseModel):
    username: str
    profilePicture: str
    bio: str


@router.get("/me")
async def getMe(user=Depends(verifyToken)):
    return await UserController.getUser(user)


@router.patch("/me")
async def updateMe(
    username: Optional[str] = Form(None),
    name: Optional[str] = Form(None),
    profilePicture: Optional[UploadFile] = File(None),
    bio: Optional[str] = Form(None),
    user=Depends(verifyToken),
):
    body = {
        "username": username,
        "name": name,
        "profilePicture": profilePicture,
        "bio": bio,
    }
    return await UserController.updateUser(user, body)
