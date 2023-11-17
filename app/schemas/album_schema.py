from typing import Optional
from pydantic import BaseModel, EmailStr
ffrom app.models.base import Base

class AlbumSchema(Base):
    id: int
    name: str | None
    artist_id: int | None
    release_date: int | None