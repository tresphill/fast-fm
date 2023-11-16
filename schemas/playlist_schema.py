from typing import Optional
from pydantic import BaseModel, EmailStr
from models.playlist_model import Base

class Base(BaseModel):
    pass

class PlaylistSchema(Base):
    id: int
    name: str | None
    user_id: str | None