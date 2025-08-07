"""
Router for Review endpoints
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas import ReviewCreate, ReviewRead, ReviewContentUpdate, ReviewVisibilityUpdate
from services.review_service import (get_user_reviews_service, get_user_work_reviews_service,
                                     get_work_reviews_service, create_review_service, delete_review_service,
                                     update_review_service, update_review_visibility_service)
from db.session import get_db


router = APIRouter()


@router.get("/user/{user_id}", status_code=status.HTTP_200_OK, response_model=list[ReviewRead])
def get_user_reviews(user_id: int, db: Session = Depends(get_db)) -> list[ReviewRead]:
    """Endpoint for get all user's reviews request
    :param user_id: integer id of user
    :param db: database session
    :return: list of Pydantic ReviewRead model objects
    """
    return get_user_reviews_service(db, user_id)


@router.get('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=list[ReviewRead])
def get_user_work_reviews(user_id: int, work_id: int, db: Session = Depends(get_db)) -> list[ReviewRead]:
    """Endpoint for get certain work and a certain user reviews request
    :param user_id: integer id of user
    :param work_id: integer id of work
    :param db: database session
    :return: Pydantic ReviewRead model object
    """
    return get_user_work_reviews_service(db, user_id, work_id)


@router.get("/work/{work_id}", status_code=status.HTTP_200_OK, response_model=list[ReviewRead])
def get_work_reviews(work_id: int, db: Session = Depends(get_db)) -> list[ReviewRead]:
    """Endpoint for get all work's reviews request
    :param work_id: integer id of work
    :param db: database session
    :return: list of Pydantic ReviewRead model objects
    """
    return get_work_reviews_service(db, work_id)


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_review(review: ReviewCreate, db: Session = Depends(get_db)) -> int:
    """Endpoint for create review object request
    :param review: Pydantic ReviewCreate model object
    :param db: database session
    :return: integer id of review
    """
    return create_review_service(db, review)


@router.delete('/delete/{review_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(review_id: int, db: Session = Depends(get_db)) -> None:
    """Endpoint for delete review object request
    :param review_id: integer id of review
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    return delete_review_service(db, review_id)


@router.patch('/update/{review_id}', status_code=status.HTTP_200_OK)
def update_review(review_id: int, comment: ReviewContentUpdate, db: Session = Depends(get_db)) -> dict[str, str]:
    """Endpoint for update review object request
    :param review_id: integer id of review
    :param comment: Pydantic ReviewContentUpdate model object
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    return update_review_service(db, review_id, comment)


@router.patch('/change_visibility/{review_id}', status_code=status.HTTP_200_OK)
def change_visibility(review_id: int, review: ReviewVisibilityUpdate, db: Session = Depends(get_db)
                      ) -> dict[str, str]:
    """Endpoint that changes visibility of review object
    :param review_id: integer id of review
    :param review: Pydantic ReviewVisibilityUpdate model object
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    return update_review_visibility_service(db, review_id, review)
