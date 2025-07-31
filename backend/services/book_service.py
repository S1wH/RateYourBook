"""
Business logic for Book and Work db models
"""
from sqlalchemy.orm import Session
from backend.schemas import (BookRead, BookCreate, BookUpdate, BookChangeApproveStatus,
                             WorkRead, WorkCreate, WorkUpdate)
from backend.models import Book, Work


def get_certain_book_service(db: Session, book_id: int) -> BookRead:
    """Function that returns a certain book by id
    :param db: database session
    :param book_id: integer id of book
    :return: BookRead model object
    """
    book = db.query(Book).get(book_id=book_id)
    return BookRead.model_validate(book)


def get_work_books_service(db: Session, work_id: int) -> list[BookRead]:
    """Function that returns all books for a certain work
    :param db: database session
    :param work_id: integer id of work
    :return: list of BookRead model objects
    """
    books = db.query(Book).filter_by(work_id=work_id)
    return [BookRead.model_validate(book) for book in books]


def get_user_books_service(db: Session, user_id: int) -> list[BookRead]:
    """Function that returns all books for a certain user
    :param db: database session
    :param user_id: integer id of user
    :return: list of BookRead model objects
    """
    books = db.query(Book).filter_by(user_id=user_id)
    return [BookRead.model_validate(book) for book in books]


def create_book_service(db: Session, book: BookCreate) -> int:
    """Function that creates Book object
    :param db: database session
    :param book: Pydantic BookCreate object
    :return: new Book object's id
    """
    db_book = Book(
        isbn=book.isbn,
        title=book.title,
        publisher=book.publisher,
        publication_year=book.publication_year,
        language=book.language,
        work_id=book.work_id,
        added_by=book.added_by,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book.id


def delete_book_service(db: Session, book_id: int) -> dict[str, str]:
    """Function that deletes Book object
    :param db: database session
    :param book_id: integer id of book
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    try:
        book = db.get(Book, book_id)
        db.delete(book)
        return {'message': 'success'}
    except Exception as e:
        return {'error': str(e)}


def update_book_service(db: Session, book_id: int, new_book: BookUpdate) -> dict[str, str]:
    """Function that changes book's metadata
    :param db: database session
    :param book_id: integer id of book
    :param new_book: Pydantic BookUpdate object
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    try:
        book = db.get(Book, book_id)
        book.isbn = new_book.isbn
        book.title = new_book.title
        book.publisher = new_book.publisher
        book.publication_year = new_book.publication_year
        book.language = new_book.language
        book.work_id = new_book.work_id

        db.commit()
        db.refresh(book)
        return {'message': 'success'}
    except Exception as e:
        return {'error': str(e)}


def change_approve_status_service(db: Session, book_id, new_book: BookChangeApproveStatus) -> dict[str, str]:
    """Function that changes approve status of book
    :param db: database session
    :param book_id: integer id of book
    :param new_book: Pydantic BookUpdate object
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    try:
        book = db.get(Book, book_id)
        book.is_approved = new_book.is_approved

        db.commit()
        db.refresh(book)
        return {'message': 'success'}
    except Exception as e:
        return {'error': str(e)}

# =====================================================================

def get_certain_work_service(db: Session, work_id: int) -> WorkRead:
    """Function that returns a certain work by id
    :param db: database session
    :param work_id: integer id of work
    :return: WorkRead model object
    """
    work = db.query(Work).get(work_id=work_id)
    return WorkRead.model_validate(work)


def get_author_works_service(db: Session, author_id: int) -> list[WorkRead]:
    """Function that returns all works for a certain author
    :param db: database session
    :param author_id: integer id of author
    :return: list of WorkRead model objects
    """
    works = db.query(Work).filter_by(author_id=author_id)
    return [WorkRead.model_validate(work) for work in works]


def create_work_service(db: Session, work: WorkCreate) -> int:
    """Function that creates Work object
    :param db: database session
    :param work: Pydantic WorkCreate object
    :return: new Work object's id
    """
    db_work = Work(
        title=work.title,
        creation_year=work.creation_year,
        description=work.description,
        author_id=work.author_id,
    )
    db.add(db_work)
    db.commit()
    db.refresh(db_work)
    return db_work.id


def delete_work_service(db: Session, work_id: int) -> dict[str, str]:
    """Function that deletes Work object
    :param db: database session
    :param work_id: integer id of work
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    try:
        work = db.get(Work, work_id)
        db.delete(work)
        return {'message': 'success'}
    except Exception as e:
        return {'error': str(e)}


def update_work_service(db: Session, work_id: int, new_work: WorkUpdate) -> dict[str, str]:
    """Function that changes Work's object metadata
    :param db: database session
    :param work_id: integer id of work
    :param new_work: Pydantic WorkUpdate object
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    try:
        work = db.get(Work, work_id)
        work.title = new_work.title,
        work.creation_year = new_work.creation_year,
        work.description = new_work.description,
        work.author_id = new_work.author_id,

        db.commit()
        db.refresh(work)
        return {'message': 'success'}
    except Exception as e:
        return {'error': str(e)}