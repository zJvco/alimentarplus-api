from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.database import Base
from app.utils import generate_uuid


role_permission = Table(
    "roles_permission",
    Base.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("uid", String(36), nullable=False, unique=True, default=lambda: generate_uuid()),
    Column("role_id", Integer, ForeignKey("roles.id"), nullable=False),
    Column("permission_id", Integer, ForeignKey("permissions.id"), nullable=False)
)


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(String(36), nullable=False, unique=True, default=lambda: generate_uuid())
    title = Column(String, nullable=False, unique=True)
    description = Column(String)
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, onupdate=func.now())

    permissions = relationship("Permission", secondary=role_permission, backref="roles")

    def __repr__(self) -> str:
        return "<Role %s>" % self.id