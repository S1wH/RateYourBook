"""
Router for Rating endpoints
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from backend.schemas import RatingCreate, RatingRead, RatingUpdate
from backend.services.rating_service import (get_user_ratings_service, get_user_work_rating_service,
                                             get_work_ratings_service, create_rating_service, delete_rating_service,
                                             update_rating_service)
from backend.db.session import get_db


router = APIRouter()


@router.get('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=list[RatingRead])
def get_user_ratings(user_id: int, db: Session = Depends(get_db)) -> list[RatingRead]:
    """Endpoint for get all user's ratings request
    :param user_id: integer id of user
    :param db: database session
    :return: list of RatingRead model objects
    """
    return get_user_ratings_service(db, user_id)


@router.get('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=RatingRead)
def get_user_work_rating(user_id: int, work_id: int, db: Session = Depends(get_db)) -> RatingRead:
    """Endpoint for get certain work and a certain user rating request
    :param user_id: integer id of user
    :param work_id: integer id os work
    :param db: database session
    :return: RatingRead model object
    """
    return get_user_work_rating_service(db, user_id, work_id)


@router.get('/work/{work_id}', status_code=status.HTTP_200_OK, response_model=list[RatingRead])
def get_work_ratings(work_id: int, db: Session = Depends(get_db)) -> list[RatingRead]:
    """Endpoint for get all work's ratings request
    :param work_id: integer id of work
    :param db: database session
    :return: list of RatingRead model objects
    """
    return get_work_ratings_service(db, work_id)


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_rating(rating: RatingCreate, db: Session = Depends(get_db)) -> int:
    """Endpoint for create rating request
    :param rating: Pydantic RatingCreate object
    :param db: database session
    :return: integer id of rating
    """
    return create_rating_service(db, rating)


@router.delete('/delete/{rating_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_rating(rating_id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    """Endpoint for delete rating object request
    :param rating_id: integer id of rating
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    return delete_rating_service(db, rating_id)


@router.patch('/update/{rating_id}', status_code=status.HTTP_200_OK)
def update_rating(rating_id: int, rating: RatingUpdate, db: Session = Depends(get_db)) -> dict[str, str]:
    """Endpoint for update rating object request
    :param rating_id: integer id of rating
    :param rating: Pydantic RatingUpdate object
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    return update_rating_service(db, rating_id, rating)
