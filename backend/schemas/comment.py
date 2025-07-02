from pydantic import BaseModel, model_validator
from typing import Optional
from datetime import datetime
from . import DiscussionShort, WorkShort, UserEveryoneRead


class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    user_id: int
    review_id: Optional[int]
    discussion_id: Optional[int]

    @model_validator(mode='after')
    def check_links(self):
        if self.discussion_id is not None and self.review_id is not None:
            raise ValueError(f'Passed both review {self.review_id} and discussion {self.discussion_id}')

    model_config = {
        "from_attributes": True
    }


class CommentRead(CommentBase):
    user: UserEveryoneRead
    review: WorkShort
    discussion: DiscussionShort
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class CommentShort(CommentBase):
    updated_at: datetime

    class Config:
        orm_mode = True


class CommentContentUpdate(BaseModel):
    content: str

    model_config = {
        "from_attributes": True
    }


class CommentVisibilityUpdate(BaseModel):
    is_hidden: bool

    model_config = {
        "from_attributes": True
    }
