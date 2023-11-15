import uuid
from pydantic import BaseModel, constr, EmailStr
from typing import Optional


class UserIn(BaseModel):
    name: str
    email: EmailStr
    phone_number: constr(min_length=11, max_length=11)
    cpf: constr(min_length=11, max_length=11)
    password: str
    is_supermarket: bool


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone_number: constr(min_length=11, max_length=11)
    cpf: constr(min_length=11, max_length=11)
    is_supermarket: bool
    is_active: bool