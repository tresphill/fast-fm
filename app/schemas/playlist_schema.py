from typing import Optional
from pydantic import BaseModel, EmailStr
from app.models.base import Base

class PlaylistSchema(Base):
    id: int
    name: str | None
    user_id: int | None