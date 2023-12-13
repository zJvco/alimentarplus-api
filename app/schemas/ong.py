from pydantic import BaseModel, ConfigDict, constr
from datetime import datetime
from typing import List, Optional

from app.schemas.address import AddressOut, AddressIn
from app.schemas.donation import DonationOut
from app.schemas.user import UserOut


class OngIn(BaseModel):
    name: str # Nome fantasia
    business_name: str # Razão Social
    state_registration: constr(min_length=8, max_length=20, pattern=r'^\d+$') # Inscrição Estadual
    phone_number: constr(min_length=11, max_length=11, pattern=r'^\d+$')
    cnpj: constr(min_length=14, max_length=14, pattern=r'^\d+$')

    address: AddressIn | None
    
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class OngOut(BaseModel):
    id: int
    name: str # Nome fantasia
    business_name: str # Razão Social
    state_registration: constr(min_length=8, max_length=20, pattern=r'^\d+$') # Inscrição Estadual
    phone_number: constr(min_length=11, max_length=11, pattern=r'^\d+$') 
    cnpj: constr(min_length=14, max_length=14, pattern=r'^\d+$') 
    created_date: datetime
    updated_date: datetime | None

    address: AddressOut
    donations: List[DonationOut]
    users: List[UserOut]

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)