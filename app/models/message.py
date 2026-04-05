from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime, timezone
from app.models.user import PyObjectId

def get_utc_now():
    return datetime.now(timezone.utc)

class MessageModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    roomId: PyObjectId
    senderId: PyObjectId
    content: str
    mediaUrl: Optional[str] = None
    createdAt: datetime = Field(default_factory=get_utc_now)

    model_config = ConfigDict(populate_by_name=True)
