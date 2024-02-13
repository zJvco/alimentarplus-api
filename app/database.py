import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

if os.getenv("ENVIRONMENT") == "development":
    engine = create_async_engine(
        os.getenv("DEV_DB_URI"),
        connect_args={"check_same_thread": False},
        echo=True
    )
elif os.getenv("ENVIRONMENT") == "production":

    if os.getenv("PROD_DB_TYPE") == "mysql":
        connection_string = f"mysql+asyncmy://{os.getenv('PROD_DB_USER')}:{os.getenv('PROD_DB_PASSWORD')}@{os.getenv('PROD_DB_HOST')}/{os.getenv('PROD_DB_NAME')}?charset=utf8mb4"
    else:
        connection_string = ""

    engine = create_async_engine(
        connection_string,
        echo=False
    )
else:
    engine = create_async_engine(
        "sqlite+aiosqlite:///./dev.db",
        connect_args={"check_same_thread": False},
        echo=True
    )

AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, autocommit=False, autoflush=False, future=True, expire_on_commit=False)
Base = declarative_base()


async def create_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)