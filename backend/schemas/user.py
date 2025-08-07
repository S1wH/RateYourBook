import re
from pydantic import BaseModel, field_validator, model_validator
from typing import Optional
from datetime import datetime



class UserBase(BaseModel):
    username: str
    bio: Optional[str]
    avatar_url: Optional[str]

    @field_validator('username')
    def username_validator(cls, username):
        if 4 > len(username) > 13:
            raise ValueError(f'ISBN {username} has incorrect length {len(username)}')
        return username


class UserCreate(BaseModel):
    email: str
    password1: str
    password2: str

    model_config = {
        "from_attributes": True
    }

    @model_validator(mode='after')
    def creation_data_validator(self):
        email_validate_pattern = r"^\S+@\S+\.\S+$"
        if re.match(self.email, email_validate_pattern) is None:
            raise ValueError(f'Email {self.email} is invalid')
        if self.discussion_id is not None and self.review_id is not None:
            raise ValueError(f'Passed both review {self.review_id} and discussion {self.discussion_id}')


class UserLogin(BaseModel):
    login: str
    password: str

    model_config = {
        "from_attributes": True
    }


class UserEveryoneRead(UserBase):
    reviews: list['ReviewRead']
    ratings: list['RatingRead']
    discussions: list['DiscussionRead']
    created_at: datetime

    model_config = {
        "from_attributes": True
    }


class UserSelfRead(UserEveryoneRead):
    email: str
    comments: list['CommentRead']

    model_config = {
        "from_attributes": True
    }
