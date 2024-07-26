from sqlalchemy.orm import Session
from schemas import BookUpdate, BookCreate
from models import BookModel


def get_book(db: Session, book_id: int):
    """
    funcao que recebe um id e retorna suas informações
    """
    return db.query(BookModel).filter(BookModel.id == book_id).first()


def get_books(db: Session):
    """
    funcao que retorna todos os elementos
    """
    return db.query(BookModel).all()


def create_book(db: Session, book: BookCreate):
    db_book = BookModel(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    db.delete(db_book)
    db.commit()
    return db_book


def update_book(db: Session, book_id: int, book: BookUpdate):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if db_book is None:
        return None

    if book.name is not None:
        db_book.name = book.name
    if book.category is not None:
        db_book.category = book.category
    if book.publisher is not None:
        db_book.publisher = book.publisher
    if book.number_of_pages is not None:
        db_book.number_of_pages = book.number_of_pages
    if book.start_reading is not None:
        db_book.start_reading = book.start_reading
    if book.end_reading is not None:
        db_book.end_reading = book.end_reading


    db.commit()
    return db_book