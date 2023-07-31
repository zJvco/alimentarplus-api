from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/register-user")
async def register_user():
    return "HI"
