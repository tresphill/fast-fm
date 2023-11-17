from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table, Numeric
from app.models.base import Base

class Artist(Base):
    __tablename__ = "artist"

    id: Column[int] = Column(primary_key = True, index = True, autoincrement="True")
    name: Column[str] = Column(String, default="name")
    genre_id: Column[int] = ForeignKey(Integer)

    