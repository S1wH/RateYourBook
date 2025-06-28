from pydantic import BaseModel, Field
from datetime import datetime
from . import WorkRead


class RatingBase(BaseModel):
    value: int = Field(..., ge=1, le=10, description='Оценка от 1 до 10')


class RatingCreate(RatingBase):
    user_id: int
    book_id: int


class RatingRead(RatingBase):
    id: int
    work_id: int
    user_id: int
    updated_at: datetime
    work: WorkRead

    class Config:
        orm_mode = True
