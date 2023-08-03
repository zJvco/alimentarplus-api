from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from datetime import timedelta

from app.models.users import User
from app.models.supermarkets import Supermarket
from app.repositories.users import UserRepository
from app.utils import verify_password, create_jwt_token
from app.dependencies import ACCESS_TOKEN_EXPIRE_MINUTES

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/register")
async def register(data: Request):
    # registrando apenas supermercado

    data = await data.json()

    user_data = data["user"]
    supermarket_data = data["supermarket"]

    user = await UserRepository.add(
        user_data["name"],
        user_data["email"],
        user_data["phone_number"],
        user_data["cpf"],
        user_data["password"]
    )

    # supermarket = 

    return data


@auth_router.post("/login")
async def login(user_data: OAuth2PasswordRequestForm = Depends()):
    email = user_data.username
    password = user_data.password

    user = await UserRepository.get_by_email(email)

    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Usuário ou senha incorretos"
        )

    token = create_jwt_token(
        {
            "sub": user.id,
            "role": user.role
        },
        timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {"token": token, "token_type": "bearer"}