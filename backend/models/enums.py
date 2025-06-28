"""
Enum classes for database models
"""
from enum import Enum


class ReadingStatus(str, Enum):
    """
    Enum for status of book for user
    """
    WANT_TO_READ = 'Хочу прочитать'
    READING = 'Читаю'
    READ = 'Прочитано'


class ReviewType(str, Enum):
    """
    Enum for review type. It can be short of long
    """
    BLITZ = 'Краткая'
    DEEP = 'Расширенная'


class Role(str, Enum):
    """
    Enum for user's role. Privileges depends on this role
    """
    READER = 'читатель'
    ADMIN = 'админ'
    AUTHOR = 'автор'


class BookRating(int, Enum):
    """
    Enum for book rating, starting with 1 and ending up with 10
    """
    pass
