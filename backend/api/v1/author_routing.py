"""
Router for Author endpoints
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas import AuthorRead, AuthorCreate, AuthorUpdate
from services.author_service import (get_author_service, get_authors_service, create_author_service,
                                             delete_author_service, update_author_service)
from db.session import get_db


router = APIRouter()


@router.get('/{author_id}', status_code=status.HTTP_200_OK, response_model=AuthorRead)
def get_author(author_id: int, db: Session = Depends(get_db)) -> AuthorRead:
    """Endpoint for get an author request
    :param author_id: integer id of author
    :param db: database session
    :return: list of AuthorRead model objects
    """
    return get_author_service(db, author_id)


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[AuthorRead])
def get_authors(db: Session = Depends(get_db)) -> list[AuthorRead]:
    """Endpoint for get all authors request
    :param db: database session
    :return: AuthorRead model object
    """
    return get_authors_service(db)


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)) -> int:
    """Endpoint for creating author request
    :param author: AuthorCreate Pydantic object
    :param db: database session
    :return: integer id of author
    """
    return create_author_service(db, author)


@router.delete('/delete/{author_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_author(author_id: int, db: Session = Depends(get_db)) -> None:
    """Endpoint for delete author object request
    :param author_id: integer id of author
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    return delete_author_service(db, author_id)


@router.patch('/update/{author_id}', status_code=status.HTTP_200_OK)
def update_autor(author_id: int, author: AuthorUpdate, db: Session = Depends(get_db)) -> dict[str, str]:
    """Endpoint for update author object request
    :param author: Pydantic AuthorUpdate model object
    :param author_id: integer id of author
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    return update_author_service(db, author_id, author)
