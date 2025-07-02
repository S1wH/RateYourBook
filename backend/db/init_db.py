"""
Script to initialize database models and dependencies
"""
from backend.db.session import engine
from backend.models.base import Base


def init_db() -> None:
    """Function to create all SqlAlchemy models
    :return:
    """
    Base.metadata.create_all(bind=engine)
