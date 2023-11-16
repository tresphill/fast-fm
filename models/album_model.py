from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table, Numeric

class Base(DeclarativeBase):
    pass

class Albums(Base):
    __tablename__ = "Albums"

    id: Mapped[int] = mapped_column(primary_key = True, index = True, autoincrement="True")
    name: Mapped[str] = Column(String, default="name")
    artist_id: Mapped[str] = Column(String, default="artist id")
    release_date: Mapped[int] = Column(Integer, default="release date")

    def __repr__(self) -> str:
        return f"Albums(id={self.id!r}, name={self.name!r}, artist_id={self.artist_id!r}, release_date={self.release_date!r})"