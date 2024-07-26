from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import BookResponse, BookUpdate, BookCreate
from typing import List
from crud import (
    create_book,
    get_books,
    get_book,
    delete_book,
    update_book,
)

router = APIRouter()


@router.post("/books/", response_model=BookResponse)
def create_book_route(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db=db, book=book)


@router.get("/books/", response_model=List[BookResponse])
def read_all_books_route(db: Session = Depends(get_db)):
    books = get_books(db)
    return books


@router.get("/books/{book_id}", response_model=BookResponse)
def read_book_route(book_id: int, db: Session = Depends(get_db)):
    db_book = get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.delete("/books/{book_id}", response_model=BookResponse)
def detele_book_route(book_id: int, db: Session = Depends(get_db)):
    db_book = delete_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.put("/books/{book_id}", response_model=BookResponse)
def update_book_route(
    book_id: int, book: BookUpdate, db: Session = Depends(get_db)
):
    db_book = update_book(db, book_id=book_id, book=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book