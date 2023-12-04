from pydantic import BaseModel, constr, EmailStr


class UserIn(BaseModel):
    name: str
    email: EmailStr
    phone_number: constr(min_length=11, max_length=11, pattern=r'^\d+$')
    cpf: constr(min_length=11, max_length=11, pattern=r'^\d+$') 
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone_number: constr(min_length=11, max_length=11, pattern=r'^\d+$') 
    cpf: constr(min_length=11, max_length=11, pattern=r'^\d+$') 
    is_active: bool
    id_supermarket: int | None
    id_ong: int | None