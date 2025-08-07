"""
Router for Work endpoints
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas import WorkRead, WorkCreate, WorkUpdate
from services.book_service import (get_certain_work_service, get_author_works_service,
                                   create_work_service, delete_work_service, update_work_service)
from db.session import get_db


router = APIRouter()


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
def delete_work(work_id: int, db: Session = Depends(get_db)) -> None:
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
