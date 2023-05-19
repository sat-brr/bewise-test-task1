import os
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

Base = declarative_base()

engine = create_async_engine(os.getenv("DB_URL"), echo=True)

async_db_session = sessionmaker(bind=engine,
                                expire_on_commit=False,
                                class_=AsyncSession)


async def get_session() -> Generator:
    try:
        session: AsyncSession = async_db_session()
        yield session
    finally:
        await session.close()


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
