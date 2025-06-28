"""
Router for Rating endpoints
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from backend.schemas import RatingCreate
from backend.db.session import get_db



router = APIRouter()


@router.get('/user/{user_id}', status_code=status.HTTP_200_OK)
async def get_user_ratings(user_id: int, db: Session = Depends(get_db)):
    pass


@router.get('/user/{user_id}', status_code=status.HTTP_200_OK)
async def get_user_work_rating(user_id: int, book_id: int, db: Session = Depends(get_db)):
    pass


@router.get('/word/{work_id}', status_code=status.HTTP_200_OK)
async def get_work_ratings(work_id: int, db: Session = Depends(get_db)):
    pass


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_rating(rating: RatingCreate, db: Session = Depends(get_db)):
    pass


@router.delete('/delete/{rating_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_rating(rating_id: int, db: Session = Depends(get_db)):
    pass


@router.patch('/update/{rating_id}', status_code=status.HTTP_200_OK)
async def update_rating(rating_id: int, score: int, db: Session = Depends(get_db)):
    pass
