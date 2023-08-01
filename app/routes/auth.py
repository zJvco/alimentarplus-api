from fastapi import APIRouter, Request

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/register")
async def register(data: Request):
    data = await data.json()
    return data


@auth_router.post("/login")
async def login():
    pass
