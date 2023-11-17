from typing import Optional
from pydantic import BaseModel, EmailStr
from app.models.base import Base

class SongSchema(Base):
    id: int
    title: str | None
    duration: int | None
    release_date: int | None
    album_id: int | None