"""
Business logic for Review db model
"""
from sqlalchemy.orm import Session
from backend.models import Review
from backend.schemas import ReviewRead, ReviewCreate, ReviewContentUpdate, ReviewVisibilityUpdate


def get_user_reviews_service(db: Session, user_id: int) -> list[ReviewRead]:
    """ Function that returns all reviews for a certain user
    :param db: database session
    :param user_id: integer id of user
    :return: list of Pydantic ReviewRead model objects
    """
    reviews = db.query(Review).filter_by(user_id=user_id).all()
    return [ReviewRead.model_validate(review) for review in reviews]


def get_user_work_reviews_service(db: Session, user_id: int, work_id: int) -> list[ReviewRead]:
    """ Function that returns reviews of a certain work for a certain user
    :param db: database session
    :param user_id: integer id of user
    :param work_id: integer id of work
    :return: list of Pydantic ReviewRead model object
    """
    reviews = db.query(Review).filter_by(user_id=user_id, work_id=work_id).all()
    return [ReviewRead.model_validate(review) for review in reviews]


def get_work_reviews_service(db: Session, work_id: int) -> list[ReviewRead]:
    """ Function that returns all reviews of a certain work
    :param db: database session
    :param work_id: integer id of work
    :return: list of Pydantic ReviewRead model objects
    """
    reviews = db.query(Review).filter_by(work_id=work_id).all()
    return [ReviewRead.model_validate(review) for review in reviews]


def create_review_service(db: Session, review: ReviewCreate) -> int:
    """Function that creates Review object
    :param db: database session
    :param review: Pydantic ReviewCreate object
    :return: new Review object id
    """
    db_review = Review(
        user_id=review.user_id,
        work_id=review.work_id,
        title=review.title,
        content=review.content,
        review_type=review.review_type
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review.id


def delete_review_service(db: Session, review_id: int) -> dict[str, str]:
    """Function that deletes review object
    :param db: database session
    :param review_id: integer id of review
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    try:
        review = db.get(Review, review_id)
        db.delete(review)
        return {'message': 'success'}
    except Exception as e:
        return {'error': str(e)}


def update_review_service(db: Session, review_id: int, new_review: ReviewContentUpdate) -> dict[str, str]:
    """Function that changes review content and/or title
    :param db: database session
    :param review_id: integer id of review
    :param new_review: Pydantic ReviewContentUpdate model object
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    try:
        review = db.get(Review, review_id)
        review.title = new_review.title
        review.content = new_review.content
        review.is_approved = False
        db.commit()
        db.refresh(review)
        return {'message': 'success'}
    except Exception as e:
        return {'error': str(e)}


def update_review_visibility_service(db: Session, review_id, new_review: ReviewVisibilityUpdate) -> dict[str, str]:
    """Function that changes review visibility
    :param db: database session
    :param review_id: integer id of review
    :param new_review: Pydantic ReviewVisibilityUpdate model object
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    try:
        review = db.get(Review, review_id)
        review.is_hidden = new_review.is_hidden
        db.commit()
        db.refresh(review)
        return {'message': 'success'}
    except Exception as e:
        return {'error': str(e)}
