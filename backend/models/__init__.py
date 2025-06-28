"""
Main SqlAlchemy models init file
"""
from .user import User, UserWork
from .book import Book, Work
from .review import Review, Comment
from .rating import Rating
from .discussion import Discussion


__all__ = [
    'User',
    'Work',
    'Book',
    'UserWork',
    'Review',
    'Rating',
    'Comment',
    'Discussion',
]
