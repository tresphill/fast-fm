from sqlalchemy.orm import Session, aliased, joinedload
from app.models import *
from app.schemas import *
from sqlalchemy import and_, or_
from app.models.song_model import Song

def get_song_items(db: Session):
    song_query = (
        db.query(Song).all()
    )
    return Song

def get_album_items(db: Session):
    albums_query = (
        db.query(Album).all()
    )
    return Albums

def get_playlist_items(db: Session):
    playlists_query = (
        db.query(Playlists).all()
    )
    return Playlists

def get_user_items(db: Session):
    user_query = (
        db.query(User).all()
    )
    return User