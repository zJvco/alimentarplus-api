from pydantic import BaseModel, ConfigDict, constr
from datetime import datetime
from typing import List

from app.schemas.address import AddressOut, AddressIn
from app.schemas.donation import DonationOut
from app.schemas.product import ProductOut
from app.schemas.user import UserOut


class SupermarketIn(BaseModel):
    name: str # Nome fantasia
    business_name: str # Razão Social
    state_registration: constr(pattern=r'^\d+$') | None = None # Inscrição Estadual, empresa pode ou não ter IE
    phone_number: constr(min_length=11, max_length=11, pattern=r'^\d+$')
    cnpj: constr(min_length=14, max_length=14, pattern=r'^\d+$')

    address: AddressIn | None = None
    # plan: PlanIn
    
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class SupermarketOut(BaseModel):
    id: int
    name: str # Nome fantasia
    business_name: str # Razão Social
    state_registration: str # Inscrição Estadual
    phone_number: constr(min_length=11, max_length=11)
    cnpj: constr(min_length=14, max_length=14)
    created_date: datetime
    updated_date: datetime | None = None

    #plan: "Plan"
    address: AddressOut
    donations: List[DonationOut]
    products:  List[ProductOut]
    users: List[UserOut]

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)