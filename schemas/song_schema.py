from typing import Optional
from pydantic import BaseModel, EmailStr
from models import Base

class Base(BaseModel):
    pass

class SongsSchema(Base):
    id: int
    title: str | None
    duration: str | None
    release_date: int | None
    album_id: int | None