from pydantic import BaseModel


class Token(BaseModel):
    token: str
    token_type: str


class TokenData(BaseModel):
    user_id: int | None = None