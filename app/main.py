from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from app.database import create_db
from app.routes.users import user_router

app = FastAPI()

app.include_router(user_router)


@app.on_event("startup")
async def startup():
    from app.models import (
        users
    )

    await create_db()