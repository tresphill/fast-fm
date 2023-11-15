from sqlalchemy.orm import Session, aliased, joinedload
from models import *
from schemas import *
from sqlalchemy import and_, or_

def get_song_items(db: Session):
    song_query = (
        db.query(Songs).all()
    )
    return Songs