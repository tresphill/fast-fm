from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table, Numeric

class Base(DeclarativeBase):
    pass

class Genre(Base):
    __tablename__ = "Playlists"

    id: Mapped[int] = mapped_column(primary_key = True, index = True, autoincrement="True")
    name: Mapped[str] = Column(String, default="name")

    def __repr__(self) -> str:
        return f"Genre(id={self.id!r}, name={self.name!r})"