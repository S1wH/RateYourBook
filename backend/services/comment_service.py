"""
Business logic for Comment db model
"""
from sqlalchemy.orm import Session
from backend.models import Comment
from backend.schemas import CommentRead, CommentCreate, CommentContentUpdate, CommentVisibilityUpdate


def get_user_comments_service(db: Session, user_id: int) -> list[CommentRead]:
    """ Function that returns all comments for a certain user
    :param db: database session
    :param user_id: integer id of user
    :return: list of PydanticCommentRead model objects
    """
    comments = db.query(Comment).filter_by(user_id=user_id).all()
    return [CommentRead.model_validate(comment) for comment in comments]


def get_user_review_comment_service(db: Session, user_id: int, review_id: int) -> CommentRead:
    """ Function that returns comment of a certain review for a certain user
    :param db: database session
    :param user_id: integer id of user
    :param review_id: integer id of review
    :return:  PydanticCommentRead model object
    """
    comment = db.query(Comment).get(user_id=user_id, review_id=review_id)
    return CommentRead.model_validate(comment)


def get_review_comments_service(db: Session, review_id: int) -> list[CommentRead]:
    """ Function that returns all comments of a certain review
    :param db: database session
    :param review_id: integer id of work
    :return: list of Pydantic CommentRead model objects
    """
    comments = db.query(Comment).filter_by(review_id=review_id).all()
    return [CommentRead.model_validate(comment) for comment in comments]


def get_user_discussion_comment_service(db: Session, user_id: int, discussion_id: int) -> CommentRead:
    """ Function that returns comment of a certain review for a certain user
    :param db: database session
    :param user_id: integer id of user
    :param discussion_id: integer id of review
    :return: Pydantic CommentRead model object
    """
    comment = db.query(Comment).get(user_id=user_id, discussion_id=discussion_id)
    return CommentRead.model_validate(comment)


def get_discussion_comments_service(db: Session, discussion_id: int) -> list[CommentRead]:
    """ Function that returns all comments of a certain review
    :param db: database session
    :param discussion_id: integer id of discussion
    :return: list of Pydantic CommentRead model objects
    """
    comments = db.query(Comment).filter_by(discussion_id=discussion_id).all()
    return [CommentRead.model_validate(comment) for comment in comments]


def create_comment_service(db: Session, comment: CommentCreate) -> int:
    """Function that creates Comment object
    :param db: database session
    :param comment: Pydantic Comment object
    :return: new Comment object id
    """
    db_comment = Comment(
        user_id=comment.user_id,
        work_id=comment.book_id,
        score=comment.score
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment.id


def delete_comment_service(db: Session, comment_id: int) -> dict[str, str]:
    """Function that deletes comment object
    :param db: database session
    :param comment_id: integer id of comment
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    try:
        comment = db.get(Comment, comment_id)
        db.delete(comment)
        return {'message': 'success'}
    except Exception as e:
        return {'error': str(e)}


def update_comment_service(db: Session, comment_id: int, new_comment: CommentContentUpdate) -> dict[str, str]:
    """Function that changes comment content
    :param db: database session
    :param comment_id: integer id of comment
    :param new_comment: Pydantic Comment model object
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    try:
        comment = db.get(Comment, comment_id)
        comment.content = new_comment.content
        db.commit()
        db.refresh(comment)
        return {'message': 'success'}
    except Exception as e:
        return {'error': str(e)}


def update_visibility_service(db: Session, comment_id, new_comment: CommentVisibilityUpdate) -> dict[str, str]:
    """Function that changes comment visibility
    :param db: database session
    :param comment_id: integer id of comment
    :param new_comment: Pydantic Comment model object
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    try:
        comment = db.get(Comment, comment_id)
        comment.is_hidden = new_comment.is_hidden
        db.commit()
        db.refresh(comment)
        return {'message': 'success'}
    except Exception as e:
        return {'error': str(e)}
