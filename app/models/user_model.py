from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table, Numeric
from app.models.base import Base

# class Base(DeclarativeBase):
#     pass

class User(Base):
    __tablename__ = "User"

    id: Column[int] = Column(primary_key = True, index = True, autoincrement="True")
    username: Column[str] = Column(String, default="username")
    email: Column[str] = Column(String, default="email")
    password: Column[str] = Column(String, default="password")

   