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

    model_config = {
        "from_attributes": True
    }


class DiscussionShort(DiscussionBase):
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class DiscussionRead(DiscussionShort):
    creator: UserEveryoneRead
    work: WorkRead
    comments: Optional[list[CommentRead]]

    model_config = {
        "from_attributes": True
    }

