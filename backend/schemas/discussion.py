from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime
from . import WorkRead, UserEveryoneRead, CommentRead


class DiscussionBase(BaseModel):
    title: str
    description: Optional[str]
    is_public: bool
    chapter_number: Optional[int]


class DiscussionCreate(DiscussionBase):
    creator_id: int
    work_id: int

    @field_validator('title')
    def title_validator(self, title):
        if 20 > len(title) > 255:
            raise ValueError(f'{title} has incorrect length {len(title)}')


class DiscussionRead(DiscussionBase):
    creator: UserEveryoneRead
    work: WorkRead
    comments: Optional[list[CommentRead]]
    updated_at: datetime

    class Config:
        orm_mode = True
