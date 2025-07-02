from pydantic import BaseModel, Field
from datetime import datetime
from . import WorkShort


class RatingBase(BaseModel):
    score: int = Field(..., ge=1, le=10, description='Оценка от 1 до 10')


class RatingCreate(RatingBase):
    user_id: int
    book_id: int

    class Config:
        orm_mode = True
        model_config = {
            'from_attributes': True
        }


class RatingRead(RatingBase):
    id: int
    work_id: int
    user_id: int
    updated_at: datetime
    work: WorkShort

    class Config:
        orm_mode = True
        model_config = {
            'from_attributes': True
        }


class RatingUpdate(RatingBase):

    class Config:
        orm_mode = True
        model_config = {
            'from_attributes': True
        }
