from pydantic import BaseModel, Field, ConfigDict, BeforeValidator
from typing import Optional, Annotated
from datetime import datetime, timezone

# PyObjectId automatically converts the MongoDB ObjectId object into a string for Pydantic.
PyObjectId = Annotated[str, BeforeValidator(str)]


def get_utc_now():
    return datetime.now(timezone.utc)


class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    email: str
    status: str
    isVerified: bool = Field(default=False)
    isOnline: bool = Field(default=False)
    username: str
    password: str  # Hashed password
    profilePicture: Optional[str] = None
    bio: Optional[str] = None
    isDeleted: bool = Field(default=False)
    updatedAt: datetime = Field(default_factory=get_utc_now)
    createdAt: datetime = Field(default_factory=get_utc_now)

    model_config = ConfigDict(populate_by_name=True)
