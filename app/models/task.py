from db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean


class Task(Base):
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(255))
  completed: Mapped[bool] = mapped_column(Boolean)