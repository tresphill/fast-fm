from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.song_schema import SongsSchema
import crud
from database import SessionLocal

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