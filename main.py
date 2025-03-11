from fastapi import Depends, FastAPI, HTTPException, status

from data_base import BOOKS
from depends import validate_book_id
from models import Book, BookRequest
from utils import set_book_id

app = FastAPI()


@app.get("/books")
async def get_books() -> list[Book]:
    return BOOKS


@app.get("/books/{book_title}")
async def get_book_by_name(book_title: str) -> Book | str:
    return next(
        (book for book in BOOKS if book["title"].lower() == book_title.lower()),
        "Not found",
    )


@app.get("/books/")
async def get_books_by_category_query(category: str) -> list[Book]:
    return [book for book in BOOKS if book["category"].lower() == category.lower()]


@app.get("/books/{book_author}/")
async def read_author_category_by_author(book_author: str, category: str) -> list[Book]:
    return [
        book
        for book in BOOKS
        if book["author"].lower() == book_author.lower()
        and book["category"].lower() == category.lower()
    ]


@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book: BookRequest) -> Book:
    new_book = set_book_id(Book(**book.model_dump()))
    BOOKS.append(new_book)
    return new_book


@app.put("/books/{id}")
async def update_book(book: BookRequest, id: int = Depends(validate_book_id)) -> Book | None:
    try:
        updated_book = Book(**book.model_dump())
        BOOKS[id] = updated_book
        return updated_book
    except IndexError:
        raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{id}")
async def delete_book(id: int = Depends(validate_book_id)) -> Book | None:
    try:
        book = BOOKS[id]
        del BOOKS[id]
        return book
    except IndexError:
        raise HTTPException(status_code=404, detail="Book not found")