from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table, Numeric

class Base(DeclarativeBase):
    pass

class Artists(Base):
    __tablename__ = "Artists"

    id: Mapped[int] = mapped_column(primary_key = True, index = True, autoincrement="True")
    name: Mapped[str] = Column(String, default="name")
    genre_id: Mapped[str] = Column(String, default="genre id")

    def __repr__(self) -> str:
        return f"Artists(id={self.id!r}, name={self.name!r}, genre_id={self.artist_id!r})"