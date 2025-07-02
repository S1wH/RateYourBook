"""
Module that provides connection data and engine for database
"""
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from backend.core.config import settings


DATABASE_URL = (f'postgresql://postgres:{settings.postgres_password}@'
                f'{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}')
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session]:
    """Returns database session connection
    :return: Generator with database Session connection
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
