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
    engine = create_async_engine(
        os.getenv("PROD_DB_URI")
    )

AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, autocommit=False, autoflush=False, future=True, expire_on_commit=False)
Base = declarative_base()


async def create_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)