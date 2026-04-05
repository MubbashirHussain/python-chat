from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime, timezone
from app.models.user import PyObjectId

def get_utc_now():
    return datetime.now(timezone.utc)

class RoomModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    isGroup: bool = False
    name: Optional[str] = None # Applicable only if isGroup is True
    participants: List[PyObjectId] = [] # List of user ObjectIds
    createdAt: datetime = Field(default_factory=get_utc_now)

    model_config = ConfigDict(populate_by_name=True)
