from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.core.base_model import BaseModel
from src.core.mixins import TimestampMixin


class User(TimestampMixin, BaseModel):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(32), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(128), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(128))
    
    def __repr__(self) -> str:
        return f"User(id='{self.id}', username='{self.username}', email='{self.email}')"