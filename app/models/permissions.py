from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey

from app.database import Base
from app.utils import generate_uuid


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(String)
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, onupdate=func.now())

    def __repr__(self) -> str:
        return "<Permission %s>" % self.id