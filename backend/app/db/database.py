from __future__ import annotations
from typing import AsyncGenerator

from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
DATABASE_URL = settings.database_url

# Create async engine
engine = create_async_engine(
    DATABASE_URL,
    future=True,
    echo=False,
    pool_pre_ping=True,
)

# Async session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# FastAPI dependency
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
