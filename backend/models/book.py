"""
Database models for Book and Work
"""
from sqlalchemy import Column, String, Integer, Boolean, Date, DateTime, Text, ForeignKey, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base


class Book(Base):
    """
    SqlAlchemy Book class
    """
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    isbn = Column(String(13), unique=True, nullable=True)
    title = Column(String(255), nullable=False)
    publisher = Column(String(100), nullable=True)
    publication_year = Column(Integer, nullable=True)
    language = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    is_approved = Column(Boolean, default=False)

    work_id = Column(Integer, ForeignKey('works.id'), nullable=False)
    added_by_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    work = relationship('Work', back_populates='books')
    added_by = relationship('User', back_populates='added_books')

    __table_args__ = (
        Index('ix_books_title', 'title'),
        Index('ix_books_language', 'language')
    )


class Work(Base):
    """
    SqlAlchemy Work class
    """
    __tablename__ = 'works'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    creation_year = Column(Date, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)

    author = relationship('Author', back_populates='works')
    books = relationship('Book', back_populates='work')
    reviews = relationship('Review', back_populates='work')
    ratings = relationship('Rating', back_populates='work')
    discussions = relationship('Discussion', back_populates='work')
    user_works = relationship('UserWork', back_populates='work')

    __table_args__ = (
        Index('ix_works_title', 'title'),
        Index('ix_works_author', 'author_id'),
    )
