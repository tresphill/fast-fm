from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table, Numeric
from app.models.base import Base

class Song(Base):
    __tablename__ = "song"

    id: Column[int] = Column(primary_key = True, index = True, autoincrement="True")
    title: Column[str] = Column(String, default="title")
    duration: Column[int] = Column(Integer)
    release_date: Column[int] = Column(Integer, default="release date")
    album_id: Column[int] = ForeignKey(Integer)

    playlist: Column[List["SongToPlaylist"]] = relationship(back_populates="song")
    artist: Column[List["ArtistToSong"]] = relationship(back_populates="artist")