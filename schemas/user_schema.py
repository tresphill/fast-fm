from typing import Optional
from pydantic import BaseModel, EmailStr
from models.user_model import Base

class Base(BaseModel):
    pass

class UserSchema(Base):
    id: int
    username: str | None
    email: str | None
    password: int | None