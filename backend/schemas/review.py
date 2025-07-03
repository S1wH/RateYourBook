from pydantic import BaseModel, field_validator
from datetime import datetime
from . import WorkShort, UserEveryoneRead, CommentShort
from backend.models.enums import ReviewType


class ReviewBase(BaseModel):
    title: str
    review_type: str
    content: str

    @field_validator('title')
    def title_validator(self, title):
        if 20 > len(title) > 255:
            raise ValueError(f'Title {title} has incorrect length {len(title)}')

    @field_validator('content')
    def content_validator(self, content):
        if len(content) > 500 and self.review_type == ReviewType.BLITZ:
            raise ValueError(f'{ReviewType.BLITZ} has incorrect length {len(content)}')
        if len(content) < 500 and self.review_type == ReviewType.DEEP:
            raise  ValueError(f'{ReviewType.DEEP} has incorrect length {len(content)}')


class ReviewCreate(ReviewBase):
    user_id: int
    work_id: int

    model_config = {
        "from_attributes": True
    }


class ReviewShort(BaseModel):
    is_approved: bool
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class ReviewRead(ReviewShort):
    user: UserEveryoneRead
    work: WorkShort
    comments: list[CommentShort]

    model_config = {
        "from_attributes": True
    }


class ReviewContentUpdate(BaseModel):
    title: str
    content: str

    model_config = {
        "from_attributes": True
    }


class ReviewVisibilityUpdate(BaseModel):
    is_hidden: bool

    model_config = {
        'from_attributes': True
    }
