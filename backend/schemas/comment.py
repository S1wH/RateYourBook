from pydantic import BaseModel, model_validator
from typing import Optional
from datetime import datetime
from .work import WorkRead
from . import DiscussionRead, UserEveryoneRead


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


class CommentRead(CommentBase):
    user: UserEveryoneRead
    review: WorkRead
    discussion: DiscussionRead
    updated_at: datetime

    class Config:
        orm_mode = True
