from pydantic import BaseModel, ConfigDict, conint
from datetime import datetime
from models.supermarkets import Supermarket
from models.ongs import Ong

 
class Address(BaseModel):

    id: int
    street: str # Rua
    number: int 
    zip_code: conint(ge=8, le=8) # CEP
    neighborhood: str # Bairro
    state: str
    city: str
    complement: str | None = None
    created_date: datetime
    updated_date: datetime

    supermarket: Supermarket
    ong: Ong
    
    model_config = ConfigDict(from_attributes=True)
