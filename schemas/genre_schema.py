from typing import Optional
from pydantic import BaseModel, EmailStr
from models.genre_model import Base

class Base(BaseModel):
    pass

class GenreSchema(Base):
    id: int
    name: str | None