from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime
from . import RatingRead, BookRead, ReviewRead, DiscussionRead


class WorkBase(BaseModel):
    title: str
    author: str
    description: Optional[str]

    @field_validator('title')
    def title_validator(self, title):
        if 20 > len(title) > 255:
            raise ValueError(f'{title} has incorrect length {len(title)}')


class WorkCreate(WorkBase):
    pass


class WorkRead(WorkBase):
    title: str
    author: str
    description: str
    books: list[BookRead]
    reviews: list[ReviewRead]
    ratings: list[RatingRead]
    discussions: list[DiscussionRead]
    updated_at: datetime

    class Config:
        orm_mode = True
