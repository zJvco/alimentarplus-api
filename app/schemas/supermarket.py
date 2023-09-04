from pydantic import BaseModel, ConfigDict, constr
from schemas.address import Address
from schemas.donations import Donations
from schemas.products import Products
#from schemas.users import User
from datetime import datetime
from typing import List


class Supermarket(BaseModel):
    id: int
    name: str # Nome fantasia
    business_name: str # Razão Social
    state_registration: str # Inscrição Estadual
    phone_number: constr(min_length=11, max_length=11)
    cnpj: constr(min_length=14, max_length=14)
    created_date: datetime
    updated_date: datetime

    #branch_office - filial do mercado
    #plan: "Plan"
    address: List[Address]
    donations: List[Donations]
    products:  List[Products]
    #users: List[User]
    
    model_config = ConfigDict(from_attributes=True)
