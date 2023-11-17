from typing import Optional
from pydantic import BaseModel, EmailStr
from app.models.base import Base

class UserSchema(Base):
    id: int
    username: str | None
    email: str | None
    password: str | None