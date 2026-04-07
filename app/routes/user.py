from fastapi import APIRouter, Depends
from pydantic import BaseModel
import app.controllers.user as UserController
from app.middlewares.auth import verifyToken

router = APIRouter(tags=["user"])


class updateMeBody(BaseModel):
    username: str
    profilePicture: str
    bio: str


@router.get("/me")
async def getMe(user=Depends(verifyToken)):
    return await UserController.getUser(user)


@router.patch("/me")
async def updateMe(body: updateMeBody, user=Depends(verifyToken)):
    return await UserController.updateUser(user, body)
