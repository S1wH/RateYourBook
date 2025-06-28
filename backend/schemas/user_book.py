from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from . import UserEveryoneRead, WorkRead


class UserWorkBase(BaseModel):
    statis: str


class UserWorkCreate(UserWorkBase):
    user_id: int
    work_id: int


class UserWorkRead(UserWorkBase):
    progress: Optional[float]
    added_at: datetime
    user: UserEveryoneRead
    work: WorkRead

    class Config:
        orm_mode = True
