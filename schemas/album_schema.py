from typing import Optional
from pydantic import BaseModel, EmailStr
from models.album_model import Base

class Base(BaseModel):
    pass

class AlbumsSchema(Base):
    id: int
    name: str | None
    artist_id: str | None
    release_date: int | None