from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from datetime import timedelta
from typing import Optional

from app.models.users import User
from app.models.supermarkets import Supermarket
from app.repositories.user import UserRepository
from app.repositories.supermarket import SupermarketRepository
from app.repositories.ong import OngRepository
from app.repositories.address import AddressRepository
from app.schemas.user import UserIn
from app.schemas.supermarket import SupermarketIn
from app.schemas.ong import OngIn
from app.utils import verify_password, create_jwt_token
from app.dependencies import ACCESS_TOKEN_EXPIRE_MINUTES

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/register")
async def register(type: str, user: UserIn, supermarket: SupermarketIn | None = None, ong: OngIn | None = None):
    try:
        created_user = await UserRepository.add(
            user
        )
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Não foi possível criar o usuário"
        )
    
    if type == "supermarket":
        # supermarket_plan = 

        try:
            address = await AddressRepository.add(
                supermarket.address
            )
        except Exception:
            # await UserRepository.delete(created_user.id)
            
            raise HTTPException(
                status_code=400,
                detail="Não foi possível cadastrar o endereço"
            )

        try:
            await SupermarketRepository.add(
                supermarket,
                created_user,
                address
            )
        except Exception:
            # print("0"*200)
            # print(created_user.id)
            # await UserRepository.delete(created_user.id)
            # await AddressRepository.delete(address.id)

            raise HTTPException(
                status_code=400,
                detail="Não foi possível cadastrar o supermercado"
            )


    elif type == "ong":
        try:
            address = await AddressRepository.add(
                ong.address
            )
        except Exception:
            # await UserRepository.delete(created_user.id)
            
            raise HTTPException(
                status_code=400,
                detail="Não foi possível cadastrar o endereço"
            )

        try:
            await OngRepository.add(
                ong,
                created_user,
                address,
            )
        except Exception:
            # await UserRepository.delete(created_user.id)
            # await AddressRepository.delete(address.id)

            raise HTTPException(
                status_code=400,
                detail="Não foi possível cadastrar a ONG"
            )

    return {"user_id": created_user.id}


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