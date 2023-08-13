import uuid
from fastapi import Depends, HTTPException
from datetime import timedelta, datetime
from jose import jwt, JWTError

from app.dependencies import pwd_context, SECRET_KEY, ALGORITHM, oauth2_scheme
from app.models.users import User


def generate_uuid() -> str:
    return str(uuid.uuid4())


def verify_password(password: str, hashed_password: str) -> str:
    return pwd_context.verify(password, hashed_password)


def generate_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_jwt_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update(
        {
            "exp": expire,
            "iat": datetime.utcnow()
        }
    )
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt


async def token_required(token: str = Depends(oauth2_scheme)) -> User:
    from app.repositories.users import UserRepository

    credentials_exception = HTTPException(
                                status_code=401,
                                detail="Não foi possível validar as credenciais"
                            )

    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)

        user_id: int = payload.get("sub")

        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = await UserRepository.get_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Usuário não existe no sistema"
        )

    return user