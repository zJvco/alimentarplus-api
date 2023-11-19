from pydantic import BaseModel, ConfigDict, constr, validator
from datetime import datetime

 
class AddressIn(BaseModel):
    street: str # Rua
    number: str 
    zip_code: constr(min_length=8, max_length=8) # CEP
    neighborhood: str # Bairro
    state: str
    city: str
    complement: str | None
    
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class AddressOut(BaseModel):
    id: int
    street: str # Rua
    number: str 
    zip_code: constr(min_length=8, max_length=8) # CEP
    neighborhood: str # Bairro
    state: str
    city: str
    complement: str | None
    created_date: datetime
    updated_date: datetime | None

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)