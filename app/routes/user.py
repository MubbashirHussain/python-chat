from fastapi import APIRouter, Depends
from pydantic import BaseModel
import app.controllers.user as UserController
from app.middlewares.auth import verifyToken

router = APIRouter(tags=["user"])


class User(BaseModel):
    id: str
    username: str
    email: str


@router.get("/me")
async def getMe(user=Depends(verifyToken)):
    return await UserController.getUser(user)
