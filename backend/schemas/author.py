from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime
from . import WorkShort


class AuthorBase(BaseModel):
    name: str
    country: str
    bio: Optional[str]

    @field_validator('name')
    def title_validator(self, name):
        if 5 > len(name) > 100:
            raise ValueError(f'Name {name} has incorrect length {len(name)}')


class AuthorCreate(AuthorBase):
    photo_url: Optional[str]
    born_date = Optional[datetime]
    death_date = Optional[datetime]

    model_config = {
        "from_attributes": True
    }


class AuthorShort(AuthorBase):
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class AuthorRead(AuthorCreate):
    works: list[WorkShort]

    model_config = {
        "from_attributes": True
    }
