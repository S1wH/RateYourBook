"""
Database model for Rating
"""
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base


class Rating(Base):
    """
    SqlAlchemy Rating class
    """
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    work_id = Column(Integer, ForeignKey('works.id'), nullable=False)
    score = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    user = relationship('User', back_populates='ratings')
    work = relationship('Work', back_populates='ratings')

    __table_args__ = (
        Index('ix_ratings_user_id', 'user_id'),
        Index('ix_ratings_work_id', 'work_id'),
        Index('ix_ratings_score', 'score')
    )
