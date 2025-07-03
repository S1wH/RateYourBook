"""
Router for Book endpoints
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from backend.schemas import (BookRead, BookCreate, BookUpdate, BookChangeApproveStatus,
                             WorkRead, WorkCreate, WorkUpdate)
from backend.services.book_service import (get_certain_book_service, get_work_books_service, get_user_books_service,
                                           create_book_service, delete_book_service, update_book_service,
                                           change_approve_status_service,
                                           get_certain_work_service, get_author_works_service, create_work_service,
                                           delete_work_service, update_work_service)
from backend.db.session import get_db


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
def delete_book(book_id: int, db: Session = Depends(get_db)) -> dict[str, str]:
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

# ==============================================================================================

@router.get('/{work_id}', status_code=status.HTTP_200_OK, response_model=WorkRead)
def get_certain_work(work_id: int, db: Session = Depends(get_db)) -> WorkRead:
    """Endpoint for get a certain work request
    :param work_id: integer id of work
    :param db: database session
    :return: Pydantic WorkRead model object
    """
    return get_certain_work_service(db, work_id)


@router.get("/author/{author_id}", status_code=status.HTTP_200_OK, response_model=list[WorkRead])
def get_author_works(author_id: int, db: Session = Depends(get_db)) -> list[WorkRead]:
    """Endpoint for get all author's works request
    :param author_id: integer id of author
    :param db: database session
    :return: list of Pydantic WorkRead model objects
    """
    return get_author_works_service(db, author_id)


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_work(work: WorkCreate, db: Session = Depends(get_db)) -> int:
    """Endpoint for create work object request
    :param work: Pydantic WorkCreate model object
    :param db: database session
    :return: integer id of work
    """
    return create_work_service(db, work)


@router.delete('/delete/{work_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_work(work_id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    """Endpoint for delete work object request
    :param work_id: integer id of work
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    return delete_work_service(db, work_id)


@router.patch('/update/{work_id}', status_code=status.HTTP_200_OK)
def update_work(work_id: int, work: WorkUpdate, db: Session = Depends(get_db)) -> dict[str, str]:
    """Endpoint for update book object request
    :param work_id: integer id of work
    :param work: Pydantic WorkUpdate model object
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    return update_work_service(db, work_id, work)
