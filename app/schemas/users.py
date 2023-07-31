from pydantic import BaseModel, constr, EmailStr
from typing import Optional


class UserCreateInput(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    cpf: constr(min_length=11, max_length=11)
    password: str