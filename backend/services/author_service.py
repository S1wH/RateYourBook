"""
Business logic for Author db model
"""
from sqlalchemy.orm import Session
from backend.schemas import AuthorRead, AuthorCreate, AuthorUpdate
from backend.models import Author


def get_author_service(db: Session, author_id: int) -> AuthorRead:
    """Function that returns a certain author
    :param author_id: integer id of user
    :param db: database session
    :return: Pydantic AuthorRead model object
    """
    author = db.get(Author, author_id)
    return AuthorRead.model_validate(author)


def get_authors_service(db: Session) -> list[AuthorRead]:
    """Function that returns all authors
    :param db: database session
    :return: list of Pydantic AuthorRead model objects
    """
    authors = db.query(Author).all()
    return [AuthorRead.model_validate(author) for author in authors]


def create_author_service(db: Session, author: AuthorCreate) -> int:
    """Function that creates Author object
    :param db: database session
    :param author: Pydantic AuthorCreate object
    :return: new Author object id
    """
    db_author = Author(
        name=author.name,
        country=author.country,
        bio=author.bio,
        photo_url=author.photo_url,
        born_date=author.born_date,
        death_date=author.death_date,
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author.id


def delete_author_service(db: Session, author_id: int) -> dict[str, str]:
    """Function that deletes Author object
    :param db: database session
    :param author_id: integer id of author
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    try:
        author = db.get(Author, author_id)
        db.delete(author)
        return {'message': 'success'}
    except Exception as e:
        return {'error': str(e)}


def update_author_service(db: Session, author_id: int, new_author: AuthorUpdate) -> dict[str, str]:
    """Function that changes author's info
    :param db: database session
    :param author_id: integer id of author
    :param new_author: Pydantic AuthorUpdate model object
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    try:
        author = db.get(Author, author_id)
        author.name = new_author.name
        author.country = new_author.country
        author.bio = new_author.bio
        author.photo_url = new_author.photo_url
        author.born_date = new_author.born_date
        author.death_date = new_author.death_date

        db.commit()
        db.refresh(author)
        return {'message': 'success'}
    except Exception as e:
        return {'error': str(e)}
