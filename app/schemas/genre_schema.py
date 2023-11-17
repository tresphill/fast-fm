from typing import Optional
from pydantic import BaseModel, EmailStr
from app.models.base import Base

class GenreSchema(Base):
    id: int
    name: str | None