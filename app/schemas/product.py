from pydantic import BaseModel, ConfigDict, constr
from datetime import datetime, date


class ProductIn(BaseModel):
    name: str
    brand: str
    description: str | None = None
    unit_weight_grams: float
    total_weight_grams: float
    quantity_units: int
    is_active: bool | None = None
    expiration_date: date
    url_product_img: str
    url_expiration_date_img: str 

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    

class ProductOut(BaseModel):
    id: int
    name: str
    brand: str
    description: str | None
    unit_weight_grams: float
    total_weight_grams: float
    quantity_units: int
    is_active: bool
    expiration_date: date
    url_product_img: str
    url_expiration_date_img: str 
    id_supermarket: int
    id_category: int | None 
    created_date: datetime
    updated_date: datetime | None

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)