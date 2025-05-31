from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column
from src.core.base_model import BaseModel
from src.core.mixins import TimestampMixin


class User(TimestampMixin, BaseModel):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(32), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(128), unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f"User(id='{self.id}', username='{self.username}', email='{self.email}')"