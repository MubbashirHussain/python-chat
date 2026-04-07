from fastapi import APIRouter
from pydantic import BaseModel
from app.routes.auth import router as auth_router
from app.routes.user import router as user_router


from fastapi import File, Form, UploadFile
from app.utils.cloudinary import uploadImages


router = APIRouter(prefix="/api")
router.include_router(auth_router, prefix="/auth")
router.include_router(user_router, prefix="/user")


class Body(BaseModel):
    username: str
    name: str


@router.post("/upload")
async def upload(username: str = Form(...), name: str = Form(...), profilePicture: UploadFile = File(...)):
    # print("debug 1", body.profilePicture)
    image_url = await uploadImages(profilePicture)
    return {"url": image_url}
