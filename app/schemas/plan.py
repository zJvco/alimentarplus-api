from pydantic import BaseModel, ConfigDict, constr
from datetime import datetime
from typing import List, Optional


class PlanIn(BaseModel):
    name: str
    price: float | None = None
    description: str | None = None

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class PlanOut(BaseModel):
    id: int
    name: str
    price: float
    description: str | None = None
    created_date: datetime
    updated_date: datetime | None = None

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class PlanInAuth(BaseException):
    id: int

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
