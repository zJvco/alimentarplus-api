from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List


class DonationIn(BaseModel):
    situation: str | None = None
    id_supermarket: int
    id_ong: int
    id_product: int

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    

class DonationOut(BaseModel):
    id: int
    situation: str | None = None
    id_supermarket: int
    id_ong: int
    id_product: int
    created_date: datetime
    updated_date: datetime | None = None

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)