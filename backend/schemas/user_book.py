from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserWorkBase(BaseModel):
    statis: str


class UserWorkCreate(UserWorkBase):
    user_id: int
    work_id: int


class UserWorkRead(UserWorkBase):
    progress: Optional[float]
    added_at: datetime
    user: 'UserEveryoneRead'
    work: 'WorkRead'

    model_config = {
        "from_attributes": True
    }
