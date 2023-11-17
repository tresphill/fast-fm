from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import crud
from database import SessionLocal
from schemas.song_schema import SongsSchema
from schemas.album_schema import AlbumsSchema
from schemas.artist_schema import ArtistsSchema
from schemas.playlist_schema import PlaylistSchema
from schemas.user_schema import UserSchema
from schemas.genre_schema import GenreSchema

router = APIRouter(
    prefix="/fast-fm"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all", response_model=List[SongsSchema])
def get_items(db: Session = Depends(get_db)):
    items = crud.get_songs_items(db)
    return items

@router.get("/all", response_model=List[AlbumsSchema])
def get_items(db: Session = Depends(get_db)):
    items = crud.get_albums_items(db)
    return items

@router.get("/all", response_model=List[ArtistsSchema])
def get_items(db: Session = Depends(get_db)):
    items = crud.get_artists_items(db)
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