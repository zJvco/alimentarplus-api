from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from app.database import create_db, AsyncSessionLocal
from app.routes.users import user_router
from app.routes.auth import auth_router
from app.models.roles import Role
from app.models.permissions import Permission

app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)


async def create_default_roles_and_permissions():
    async with AsyncSessionLocal() as session:
        role1 = {
            "title": "admin",
            "description": "No coments"
        }

        permission1 = {
            ""
        }
        

@app.on_event("startup")
async def startup():
    from app.models import (
        users,
        roles,
        permissions,
        supermarkets,
        ongs,
        addresses,
        products,
        donations,
        categories,
        plans
    )

    await create_db()