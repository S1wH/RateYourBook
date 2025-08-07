"""
Script to initialize database models and dependencies
"""
from db.session import engine
from models.base import Base


def init_db() -> None:
    """Function to create all SqlAlchemy models
    :return:
    """
    Base.metadata.create_all(bind=engine)
