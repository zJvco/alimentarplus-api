from pydantic import BaseModel, ConfigDict, constr, validator
from datetime import datetime
from typing import Optional

 
class AddressIn(BaseModel):
    street: str # Rua
    number: str 
    zip_code: constr(min_length=8, max_length=8) # CEP
    neighborhood: str # Bairro
    state: str
    city: str
    complement: str | None = None
    
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class AddressOut(BaseModel):
    id: int
    street: str # Rua
    number: str 
    zip_code: constr(min_length=8, max_length=8) # CEP
    neighborhood: str # Bairro
    state: str
    city: str
    complement: str | None = None
    created_date: datetime
    updated_date: Optional[datetime]

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)