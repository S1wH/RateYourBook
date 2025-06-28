"""
Database models for User and UserWork
"""
from sqlalchemy import Column, Integer, Float, String, Text, DateTime, ForeignKey, Index, Enum, func
from sqlalchemy.orm import relationship
from .base import Base
from .enums import Role, ReadingStatus


class User(Base):
    """
    SqlAlchemy User class
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(Role), default=Role.READER, nullable=False)
    bio = Column(Text, nullable=True)
    avatar_url = Column(String, nullable=True)
    registered_at = Column(DateTime(timezone=True), server_default=func.now())

    reviews = relationship('Review', back_populates='user')
    ratings = relationship('Rating', back_populates='user')
    comments = relationship('Comment', back_populates='user')
    discussions = relationship('Discussion', back_populates='creator')
    user_works = relationship('UserWorks', back_populates='user')

    __table_args__ = (
        Index('ix_users_username', 'username'),
        Index('ix_users_email', 'email'),
    )


class UserWork(Base):
    """
    SqlAlchemy UserWork class
    """
    __tablename__ = 'user_books'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    work_id = Column(Integer, ForeignKey('works.id'), nullable=False)
    status = Column(Enum(ReadingStatus), nullable=False)
    progress = Column(Float, default=0.0, nullable=True)
    added_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    user = relationship('User', back_populates='user_works')
    work = relationship('Work', back_populates='user_works')

    __table_args__ = (
        Index('ix_user_books_user_id', 'user_id'),
        Index('ix_user_works_work_id', 'work_id'),
    )
