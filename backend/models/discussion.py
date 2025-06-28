"""
Database model for Discussion
"""
from sqlalchemy import Column, String, Text, Boolean, Integer, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base


class Discussion(Base):
    """
    SqlAlchemy Discussion class
    """
    __tablename__ = 'discussions'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    creator_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    work_id = Column(Integer, ForeignKey('works.id'), nullable=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    is_public = Column(Boolean, default=True)
    chapter_number = Column(Integer, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    creator = relationship('User', back_populates='discussions')
    work = relationship('Work', back_populates='discussions')
    comments = relationship('Comment', back_populates='discussion')

    __table_args__ = (
        Index('ix_discussions_creator_id', 'creator_id'),
        Index('ix_discussions_work_id', 'work_id'),
    )
