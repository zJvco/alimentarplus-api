from pydantic import BaseModel, ConfigDict
from datetime import datetime
from models.products import Product
from typing import List


class Categories(BaseModel):

    id: int
    name: str
    created_date: datetime
    updated_date: datetime

    products: List[Product]

    model_config = ConfigDict(from_attributes=True)
