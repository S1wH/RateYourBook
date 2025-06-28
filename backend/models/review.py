"""
Database models for Review and Comment
"""
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Index, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base
from .enums import ReviewType


# TODO: Make ABS class for Review and Comment


class Review(Base):
    """
    SalAlchemy Review class
    """
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    work_id = Column(Integer, ForeignKey('works.id'), nullable=False)
    title = Column(String(50), nullable=False)
    review_type = Column(Enum(ReviewType), nullable=False)
    content = Column(Text, nullable=False)
    is_approved = Column(Boolean, default=True)
    is_hidden = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    user = relationship('User', back_populates='reviews')
    work = relationship('Work', back_populates='reviews')
    comments = relationship('Comment', back_populates='review')

    __table_args__ = (
        Index('ix_reviews_user_id', 'user_id'),
        Index('ix_reviews_work_id', 'work_id'),
    )


class Comment(Base):
    """
    SqlAlchemy Comment class
    """
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    review_id = Column(Integer, ForeignKey('reviews.id'), nullable=True)
    discussion_id = Column(Integer, ForeignKey('discussions.id'), nullable=True)
    content = Column(Text, nullable=False)
    is_hidden = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    user = relationship('User', back_populates='comments')
    review = relationship('Review', back_populates='comments')
    discussion = relationship('Discussion', back_populates='comments')

    __table_args__ = (
        Index('ix_comments_user_id', 'user_id'),
        Index('ix_comments_review_id', 'review_id'),
        Index('ix_comments_discussion_id', 'discussion_id'),
    )
