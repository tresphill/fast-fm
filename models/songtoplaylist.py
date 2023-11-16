from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table, Numeric

class Base(DeclarativeBase):
    pass

class SongToPlaylist(Base):
    __tablename__ = "SongToPlaylist"

    id: Mapped[int] = mapped_column(primary_key = True, index = True, autoincrement="True")
    playlist_id: Mapped[str] = Column(String, default="playlist id")
    song_id: Mapped[str] = Column(String, default="song id")

    def __repr__(self) -> str:
        return f"SongToPlaylist(id={self.id!r}, playlist_id={self.playlist_id!r}, song_id={self.song_id!r})"