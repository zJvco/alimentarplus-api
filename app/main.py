from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from app.database import create_db
from app.routes.user_route import user_router

app = FastAPI()

app.include_router(user_router)


@app.on_event("startup")
async def startup():
    from app.models.user_model import User
    
    await create_db()