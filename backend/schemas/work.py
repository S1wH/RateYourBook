from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime
from . import RatingShort, BookShort, ReviewShort, DiscussionShort, AuthorShort


class WorkBase(BaseModel):
    title: str
    creation_year: Optional[datetime]
    description: Optional[str]

    @field_validator('title')
    def title_validator(self, title):
        if 20 > len(title) > 255:
            raise ValueError(f'Title {title} has incorrect length {len(title)}')


class WorkCreate(WorkBase):
    author_id: int

    model_config = {
        "from_attributes": True
    }


class WorkShort(WorkBase):
    author: AuthorShort
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class WorkRead(WorkShort):
    books: list[BookShort]
    reviews: list[ReviewShort]
    ratings: list[RatingShort]
    discussions: list[DiscussionShort]

    model_config = {
        "from_attributes": True
    }


class WorkUpdate(WorkCreate):

    model_config = {
        "from_attributes": True
    }
