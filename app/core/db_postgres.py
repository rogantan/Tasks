from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from db.base import Base
from core.config import settings
from fastapi import Depends
from typing import Annotated

DATABASE_URL = str(settings.database_url)

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def create_db_and_tables():
  async with engine.begin() as connection:
    await connection.run_sync(Base.metadata.create_all)

async def get_session():
  async with async_session() as session:
    yield session

CurrentSession = Annotated[AsyncSession, Depends(get_session)]