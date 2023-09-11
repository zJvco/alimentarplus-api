from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.models.supermarkets import Supermarket
from app.models.ongs import Ong
from app.models.products import Product
from typing import List


class Donations(BaseModel):
    id: int
    uid: str
    situation: str | None = None
    id_supermarket: int
    id_ong: int
    id_product: int
    created_date: datetime
    updated_date: datetime

    supermarket: Supermarket
    ong: Ong
    product: List[Product]

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    