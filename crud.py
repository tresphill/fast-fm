from sqlalchemy.orm import Session, aliased, joinedload
from models import *
from schemas import *
from sqlalchemy import and_, or_
from models.song_model import Songs

def get_songs_items(db: Session):
    song_query = (
        db.query(Songs).all()
    )
    return Songs

def get_albums_items(db: Session):
    albums_query = (
        db.query(Albums).all()
    )
    return Albums

def get_playlist_items(db: Session):
    playlists_query = (
        db.query(Playlists).all()
    )
    return Playlists