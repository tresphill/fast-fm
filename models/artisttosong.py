from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table, Numeric

class Base(DeclarativeBase):
    pass

class ArtistToSong(Base):
    __tablename__ = "ArtistToSong"

    id: Mapped[int] = mapped_column(primary_key = True, index = True, autoincrement="True")
    artist_id: Mapped[str] = Column(String, default="artist is")
    song_id: Mapped[str] = Column(String, default="song id")

    def __repr__(self) -> str:
        return f"ArtistToSong(id={self.id!r}, artist_id={self.artist_id!r}, song_id={self.song_id!r})"