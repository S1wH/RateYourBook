from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime
from . import WorkShort


class BookBase(BaseModel):
    isbn: Optional[str]
    title: str
    publisher: Optional[str]
    publication_year: Optional[str]
    language: str

    @field_validator('isbn')
    def isbn_validator(self, isbn):
        if isbn and len(isbn) > 13:
            raise ValueError(f'ISBN {isbn} has incorrect length {len(isbn)}')

    @field_validator('title')
    def title_validator(self, title):
        if 20 > len(title) > 255:
            raise ValueError(f'Title {title} has incorrect length {len(title)}')

    @field_validator('publisher')
    def publisher_validator(self, publisher):
        if len(publisher) > 100:
            raise ValueError(f'Publisher {publisher} has incorrect length {len(publisher)}')

    @field_validator('language')
    def language_validator(self, language):
        if len(language) > 50:
            raise ValueError(f'Language {language} has incorrect length {len(language)}')


class BookCreate(BookBase):
    work_id: int
    added_by: int

    model_config = {
        "from_attributes": True
    }


class BookShort(BookBase):
    is_approved: bool
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class BookRead(BookShort):
    work: WorkShort

    model_config = {
        "from_attributes": True
    }


class BookUpdate(BookBase):
    work_id: int

    model_config = {
        "from_attributes": True
    }


class BookChangeApproveStatus(BaseModel):
    is_approved: bool

    model_config = {
        "from_attributes": True
    }
