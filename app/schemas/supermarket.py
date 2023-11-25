from pydantic import BaseModel, ConfigDict, constr
from datetime import datetime
from typing import List, Optional, Dict

from app.schemas.address import AddressOut, AddressIn
from app.schemas.donation import DonationOut
from app.schemas.product import ProductOut
from app.schemas.user import UserOut


class SupermarketIn(BaseModel):
    name: str # Nome fantasia
    business_name: str # Razão Social
    state_registration: str # Inscrição Estadual
    phone_number: constr(min_length=11, max_length=11)
    cnpj: constr(min_length=14, max_length=14)

    address: AddressIn | None
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
    updated_date: datetime | None

    #plan: "Plan"
    address: AddressOut
    donations: List[DonationOut]
    products:  List[ProductOut]
    users: List[UserOut]

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)