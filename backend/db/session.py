"""
Module that provides connection data and engine for database
"""
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


#TODO: create from app.core.config
DATABASE_URL = "postgresql://user:password@localhost/dbname"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


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
