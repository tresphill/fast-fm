from typing import Optional
from pydantic import BaseModel, EmailStr
from models.artist_model import Base

class Base(BaseModel):
    pass

class ArtistsSchema(Base):
    id: int
    name: str | None
    genre_id: str | None