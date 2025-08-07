"""
Module that provides connection data and engine for database
"""
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from core.config import postgres_settings


DATABASE_URL = postgres_settings.database_url
engine = create_engine(DATABASE_URL)

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
