from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from datetime import timedelta

from app.models.users import User
from app.models.supermarkets import Supermarket
from app.repositories.users import UserRepository
from app.repositories.supermarkets import SupermarketRepository
from app.repositories.ongs import OngRepository
from app.repositories.address import AddressRepository
from app.utils import verify_password, create_jwt_token
from app.dependencies import ACCESS_TOKEN_EXPIRE_MINUTES

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/register")
async def register(type: str, data: Request):
    data = await data.json()

    try:
        user_data = data["user"]
        org_data = data["org"] # Supermercado/ONG
    except KeyError as ex:
        HTTPException(
            status_code=400,
            detail="A estrutura JSON enviada não corresponde ao esperado pelo servidor"
        )

    user = await UserRepository.add(
        user_data["name"],
        user_data["email"],
        user_data["phone_number"],
        user_data["cpf"],
        user_data["password"]
    )

    org_address = await AddressRepository.add(
        org_data["address"]["street"],
        org_data["address"]["number"],
        org_data["address"]["zip_code"],
        org_data["address"]["neighborhood"],
        org_data["address"]["state"],
        org_data["address"]["city"],
        org_data["address"]["complement"]
    )

    if type == "supermarket":
        # supermarket_plan = 

        await SupermarketRepository.add(
            org_data["metadata"]["name"],
            org_data["metadata"]["business_name"],
            org_data["metadata"]["state_registration"],
            org_data["metadata"]["phone_number"],
            org_data["metadata"]["cnpj"],
            org_address,
            user
        )
    elif type == "ong":
        await OngRepository.add(
            org_data["metadata"]["name"],
            org_data["metadata"]["business_name"],
            org_data["metadata"]["state_registration"],
            org_data["metadata"]["phone_number"],
            org_data["metadata"]["cnpj"],
            org_address,
            user
        )

    return {"user_id": user.id}


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
            "sub": str(user.id),
            # "role": user.role
        },
        timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {"token": token, "token_type": "bearer"}