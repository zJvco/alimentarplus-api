from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.models.products import Product
from typing import List


class CategoryIn(BaseModel):

    id: int
    name: str
    created_date: datetime
    updated_date: datetime

    products: List[Product]

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class CategoryOut(BaseModel):
    id: int
    name: str
    created_date: datetime
    updated_date: datetime

    products: List[Product]
