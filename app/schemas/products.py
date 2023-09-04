from pydantic import BaseModel, ConfigDict
from datetime import datetime
from models.supermarkets import Supermarket
from models.categories import Category
from models.donations import Donation
 
class Products(BaseModel):
    id: int
    uid: str
    name: str
    brand: str
    description: str | None = None
    unit_weight_grams: str
    total_weight_grams: str
    quantity_units: int
    is_active: bool
    expiration_date: datetime
    url_product_img: str
    url_expiration_date_img: str 
    id_supermarket: int
    id_category: int
    created_date: datetime
    updated_date:datetime

    supermarket: Supermarket
    category: Category
    donation: Donation

    model_config = ConfigDict(from_attributes=True)
    