"""
Router for Comment endpoints
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from backend.schemas import CommentCreate, CommentRead, CommentContentUpdate, CommentVisibilityUpdate
from backend.services.comment_service import (get_user_comments_service, get_user_review_comment_service,
                                              get_review_comments_service, get_user_discussion_comment_service,
                                              get_discussion_comments_service, create_comment_service,
                                              delete_comment_service, update_comment_service,
                                              update_comment_visibility_service)
from backend.db.session import get_db


router = APIRouter()


@router.get("/user/{user_id}", status_code=status.HTTP_200_OK, response_model=list[CommentRead])
def get_user_comments(user_id: int, db: Session = Depends(get_db)) -> list[CommentRead]:
    """Endpoint for get all user's comments request
    :param user_id: integer id of user
    :param db: database session
    :return: list of Pydantic CommentRead model objects
    """
    return get_user_comments_service(db, user_id)


@router.get('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=CommentRead)
def get_user_review_comment(user_id: int, review_id: int, db: Session = Depends(get_db)) -> list[CommentRead]:
    """Endpoint for get certain review and a certain user comment request
    :param user_id: integer id of user
    :param review_id: integer id of review
    :param db: database session
    :return: Pydantic CommentRead model object
    """
    return get_user_review_comment_service(db, user_id, review_id)


@router.get("/review/{review_id}", status_code=status.HTTP_200_OK, response_model=list[CommentRead])
def get_review_comments(review_id: int, db: Session = Depends(get_db)) -> list[CommentRead]:
    """Endpoint for get all review's comments request
    :param review_id: integer id of review
    :param db: database session
    :return: list of Pydantic CommentRead model objects
    """
    return get_review_comments_service(db, review_id)


@router.get('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=CommentRead)
def get_user_discussion_comment(user_id: int, discussion_id: int, db: Session = Depends(get_db)) -> list[CommentRead]:
    """Endpoint for get certain discussion and a certain user comments request
    :param user_id: integer id of user
    :param discussion_id: integer id of discussion
    :param db: database session
    :return: Pydantic CommentRead model object
    """
    return get_user_discussion_comment_service(db, user_id, discussion_id)


@router.get("/discussion/{discussion_id}", status_code=status.HTTP_200_OK, response_model=list[CommentRead])
def get_discussion_comments(discussion_id: int, db: Session = Depends(get_db)) -> list[CommentRead]:
    """Endpoint for get all discussion's comments request
    :param discussion_id: integer id of discussion
    :param db: database session
    :return: list of Pydantic CommentRead model objects
    """
    return get_discussion_comments_service(db, discussion_id)


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)) -> int:
    """Endpoint for create comment object request
    :param comment: Pydantic CommentCreate model object
    :param db: database session
    :return: integer id of comment
    """
    return create_comment_service(db, comment)


@router.delete('/delete/{comment_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(comment_id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    """Endpoint for delete comment object request
    :param comment_id: integer id of comment
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    return delete_comment_service(db, comment_id)


@router.patch('/update/{comment_id}', status_code=status.HTTP_200_OK)
def update_comment(comment_id: int, comment: CommentContentUpdate, db: Session = Depends(get_db)) -> dict[str, str]:
    """Endpoint for update comment object request
    :param comment_id: integer id of comment
    :param comment: Pydantic CommentContentUpdate model object
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    return update_comment_service(db, comment_id, comment)


@router.patch('/change_visibility/{comment_id}', status_code=status.HTTP_200_OK)
def change_comment_visibility(comment_id: int, comment: CommentVisibilityUpdate, db: Session = Depends(get_db)
                      ) -> dict[str, str]:
    """Endpoint that changes visibility of comment object
    :param comment_id: integer id of comment
    :param comment: Pydantic CommentVisibilityUpdate model object
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    return update_comment_visibility_service(db, comment_id, comment)
