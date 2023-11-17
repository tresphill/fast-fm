from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table, Numeric
from app.models.base import Base

class Album(Base):
    __tablename__ = "album"

    id: Column[int] = Column(primary_key = True, index = True, autoincrement="True")
    name: Column[str] = Column(String, default="name")
    artist_id: Column[int] = ForeignKey(Integer)
    release_date: Column[int] = Column(Integer, default="release date")