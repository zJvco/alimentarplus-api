from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey

from app.database import Base
from app.utils import generate_uuid


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, onupdate=func.now())

    def __repr__(self) -> str:
        return "<Category %s>" % self.id