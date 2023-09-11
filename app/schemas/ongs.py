from pydantic import BaseModel, ConfigDict, constr
from datetime import datetime
from typing import List, Optional

from app.schemas.address import AddressOut, AddressIn
from app.schemas.donations import Donations
from app.schemas.users import UserOut


class OngIn(BaseModel):
    name: str # Nome fantasia
    business_name: str # Razão Social
    state_registration: str # Inscrição Estadual
    phone_number: constr(min_length=11, max_length=11)
    cnpj: constr(min_length=14, max_length=14)

    address: Optional[AddressIn]
    # plan: PlanIn
    
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class OngOut(BaseModel):
    id: int
    name: str # Nome fantasia
    business_name: str # Razão Social
    state_registration: str # Inscrição Estadual
    phone_number: constr(min_length=11, max_length=11)
    cnpj: constr(min_length=14, max_length=14)
    created_date: datetime
    updated_date: Optional[datetime]

    address: AddressOut
    donations: List[Donations]
    users: List[UserOut]

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)