from fastapi import FastAPI

from data_base import BOOKS
from models import Book

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
