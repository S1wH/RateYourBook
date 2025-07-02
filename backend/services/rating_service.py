"""
Business logic for Rating db model
"""
from sqlalchemy.orm import Session
from backend.models import Rating
from backend.schemas import RatingRead, RatingCreate, RatingUpdate


def get_user_ratings_service(db: Session, user_id: int) -> list[RatingRead]:
    """ Function that returns all ratings for a certain user
    :param db: database session
    :param user_id: integer id of user
    :return: list of RatingRead model objects
    """
    ratings = db.query(Rating).filter_by(user_id=user_id).all()
    return [RatingRead.model_validate(rating) for rating in ratings]


def get_user_work_rating_service(db: Session, user_id: int, work_id: int) -> RatingRead:
    """ Function that returns rating of a certain work for a certain user
    :param db: database session
    :param user_id: integer id of user
    :param work_id: integer id of work
    :return: RatingRead model object
    """
    rating = db.query(Rating).get(user_id=user_id, work_id=work_id)
    return RatingRead.model_validate(rating)


def get_work_ratings_service(db: Session, work_id: int) -> list[RatingRead]:
    """ Function that returns all ratings of a certain work
    :param db: database session
    :param work_id: integer id of work
    :return: list of RatingRead model objects
    """
    ratings = db.query(Rating).filter_by(work_id=work_id).all()
    return [RatingRead.model_validate(rating) for rating in ratings]


def create_rating_service(db: Session, rating: RatingCreate) -> int:
    """Function that creates Rating object
    :param db: database session
    :param rating: Pydantic Rating object
    :return: new Rating object id
    """
    db_rating = Rating(
        user_id=rating.user_id,
        work_id=rating.book_id,
        score=rating.score
    )
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating.id


def delete_rating_service(db: Session, rating_id: int) -> dict[str, str]:
    """Function that deletes Rating object
    :param db: database session
    :param rating_id: integer id of rating
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    try:
        rating = db.get(Rating, rating_id)
        db.delete(rating)
        return {'message': 'success'}
    except Exception as e:
        return {'error': str(e)}


def update_rating_service(db: Session, rating_id: int, new_rating: RatingUpdate) -> dict[str, str]:
    """Function that changes rating score
    :param db: database session
    :param rating_id: integer id of rating
    :param new_rating: Pydantic rating object
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    try:
        rating = db.get(Rating, rating_id)
        rating.score = new_rating.score
        db.commit()
        db.refresh(rating)
        return {'message': 'success'}
    except Exception as e:
        return {'error': str(e)}
