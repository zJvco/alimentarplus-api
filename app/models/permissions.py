from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.roles import role_permission


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False, unique=True)
    description = Column(String(255))
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, onupdate=func.now())

    roles = relationship("Role", secondary=role_permission, back_populates="permissions", lazy='selectin')

    def __repr__(self) -> str:
        return "<Permission %s>" % self.id