from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from collections.abc import AsyncGenerator

from app.core.config import get_settings

settings = get_settings()

# create a engine/connection pool
engine = create_async_engine(settings.database_url, echo=False)

# create db session factory , so it knows how to create a session using an engine
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

# give each request a db session
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with  async_session_maker() as session:
        yield session