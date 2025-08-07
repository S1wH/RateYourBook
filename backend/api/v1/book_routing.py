"""
Router for Book endpoints
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas import BookRead, BookCreate, BookUpdate, BookChangeApproveStatus
from services.book_service import (get_certain_book_service, get_work_books_service, get_user_books_service, 
                                   create_book_service, delete_book_service, update_book_service,
                                   change_approve_status_service)
from db.session import get_db


router = APIRouter()


@router.get('/{book_id}', status_code=status.HTTP_200_OK, response_model=BookRead)
def get_certain_book(book_id: int, db: Session = Depends(get_db)) -> BookRead:
    """Endpoint for get a certain book request
    :param book_id: integer id of book
    :param db: database session
    :return: Pydantic BookRead model object
    """
    return get_certain_book_service(db, book_id)


@router.get("/work/{work_id}", status_code=status.HTTP_200_OK, response_model=list[BookRead])
def get_work_books(work_id: int, db: Session = Depends(get_db)) -> list[BookRead]:
    """Endpoint for get all work's books request
    :param work_id: integer id of work
    :param db: database session
    :return: list of Pydantic BookRead model objects
    """
    return get_work_books_service(db, work_id)


@router.get("/user/{user_id}", status_code=status.HTTP_200_OK, response_model=list[BookRead])
def get_user_books(user_id: int, db: Session = Depends(get_db)) -> list[BookRead]:
    """Endpoint for get all user's books request
    :param user_id: integer id of user
    :param db: database session
    :return: list of Pydantic BookRead model objects
    """
    return get_user_books_service(db, user_id)


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)) -> int:
    """Endpoint for create book object request
    :param book: Pydantic BookCreate model object
    :param db: database session
    :return: integer id of book
    """
    return create_book_service(db, book)


@router.delete('/delete/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)) -> None:
    """Endpoint for delete book object request
    :param book_id: integer id of book
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    return delete_book_service(db, book_id)


@router.patch('/update/{book_id}', status_code=status.HTTP_200_OK)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)) -> dict[str, str]:
    """Endpoint for update book object request
    :param book_id: integer id of book
    :param book: Pydantic BookUpdate model object
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    return update_book_service(db, book_id, book)


@router.patch('/change_approve_status/{book_id}', status_code=status.HTTP_200_OK)
def change_approve_status(book_id: int, book: BookChangeApproveStatus, db: Session = Depends(get_db)
                          ) -> dict[str, str]:
    """Endpoint that changes approve status of book object
    :param book_id: integer id of book
    :param book: Pydantic BookChangeApproveStatus model object
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    return change_approve_status_service(db, book_id, book)
