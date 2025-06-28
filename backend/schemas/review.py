from pydantic import BaseModel, field_validator
from datetime import datetime
from . import WorkRead, UserEveryoneRead, CommentRead


class ReviewBase(BaseModel):
    title: str
    review_type: str
    content: str

    @field_validator('title')
    def title_validator(self, title):
        if 20 > len(title) > 255:
            raise ValueError(f'{title} has incorrect length {len(title)}')


class ReviewCreate(ReviewBase):
    user_id: int
    work_id: int


class ReviewRead(ReviewBase):
    is_approved: bool
    user: UserEveryoneRead
    work: WorkRead
    comments: list[CommentRead]
    updated_at: datetime

    class Config:
        orm_mode = True
