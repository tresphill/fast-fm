from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table, Numeric

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key = True, index = True, autoincrement="True")
    username: Mapped[str] = Column(String, default="username")
    email: Mapped[str] = Column(String, default="email")
    password: Mapped[int] = Column(Integer, default="password")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, email={self.email!r}, password={self.password!r})"