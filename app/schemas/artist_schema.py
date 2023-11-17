from typing import Optional
from pydantic import BaseModel, EmailStr
from app.models.base import Base

class ArtistSchema(Base):
    id: int
    name: str | None
    genre_id: int | None