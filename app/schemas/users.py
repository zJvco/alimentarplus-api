from pydantic import BaseModel, Field
from typing import Optional


class UserCreateInput(BaseModel):
    name: str
    email: str
    phone_number: str
    cpf: str = Field(..., max_length=11)
    password: str