from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import app.crud
from database import SessionLocal
from app.schemas.song_schema import SongSchema
from app.schemas.album_schema import AlbumSchema
from app.schemas.artist_schema import ArtistSchema
from app.schemas.playlist_schema import PlaylistSchema
from app.schemas.user_schema import UserSchema
from app.schemas.genre_schema import GenreSchema

router = APIRouter(
    prefix="/fast-fm"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all", response_model=List[SongSchema])
def get_items(db: Session = Depends(get_db)):
    items = crud.get_song_items(db)
    return items

@router.get("/all", response_model=List[AlbumSchema])
def get_items(db: Session = Depends(get_db)):
    items = crud.get_album_items(db)
    return items

@router.get("/all", response_model=List[ArtistSchema])
def get_items(db: Session = Depends(get_db)):
    items = crud.get_artist_items(db)
    return items

@router.get("/all", response_model=List[PlaylistSchema])
def get_items(db: Session = Depends(get_db)):
    items = crud.get_playlist_items(db)
    return items

@router.get("/all", response_model=List[UserSchema])
def get_items(db: Session = Depends(get_db)):
    items = crud.get_user_items(db)
    return items

@router.get("/all", response_model=List[GenreSchema])
def get_items(db: Session = Depends(get_db)):
    items = crud.get_genre_items(db)
    return items