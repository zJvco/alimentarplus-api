from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()

from app.database import create_db, AsyncSessionLocal
from app.routes.users import user_router
from app.routes.auth import auth_router
from app.routes.supermarkets import supermarket_router
from app.models.roles import Role
from app.models.permissions import Permission

app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(supermarket_router)


# async def create_default_roles_and_permissions():
#     async with AsyncSessionLocal() as session:
#         role1 = {
#             "title": "admin",
#             "description": "No coments"
#         }

#         permission1 = {
#             ""
#         }

    
@app.exception_handler(Exception)
async def generic_error(request, ex):
    # Alterar depois para poder loggar tudo que é erro
    return JSONResponse(status_code=500, content={"detail": f"Erro inesperado ocorreu no servidor: {ex}"})
        

@app.on_event("startup")
async def startup():
    from app.models import ( # Aqui ele vai importar e criar todas as tabelas em /models
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