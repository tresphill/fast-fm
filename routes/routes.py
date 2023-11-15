from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import schemas
import crud
from session import SessionLocal

router = APIRouter(
    prefix="/fast-fm"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all", response_model=List[schemas.FastFMSchema])
def get_items(db: Session = Depends(get_db)):
    items = crud.get_songs_items(db)
    return items