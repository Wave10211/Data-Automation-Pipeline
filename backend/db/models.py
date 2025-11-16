# backend/db/models.py
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Boolean, DateTime, func

Base = declarative_base()

class TodoRecord(Base):
    __tablename__ = "todos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    external_id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    title: Mapped[str] = mapped_column(String(512), nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    fetched_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
