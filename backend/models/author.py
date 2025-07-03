"""
Database model for Author
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, Index, func, Date
from sqlalchemy.orm import relationship
from .base import Base


class Author(Base):
    """
    SqlAlchemy Author class
    """
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    photo_url = Column(String(255), nullable=True)
    country = Column(String(100), nullable=False)
    bio = Column(Text, nullable=True)
    born_date = Column(Date, nullable=True)
    death_date = Column(Date, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    works = relationship('Work', back_populates='author')

    __table_args__ = (
        Index('ix_authors_name', 'name'),
    )
