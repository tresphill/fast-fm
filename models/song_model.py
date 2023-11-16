from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table, Numeric

class Base(DeclarativeBase):
    pass

class Songs(Base):
    __tablename__ = "Songs"

    id: Mapped[int] = mapped_column(primary_key = True, index = True, autoincrement="True")
    title: Mapped[str] = Column(String, default="title")
    duration: Mapped[str] = Column(String, default="duration")
    release_date: Mapped[int] = Column(Integer, default="release date")
    album_id: Mapped[int] = Column(Integer, default="Zone")

    def __repr__(self) -> str:
        return f"Songs(id={self.id!r}, title={self.title!r}, duration={self.duration!r}, release_date={self.release_date!r}, album_id={self.album_id!r})"