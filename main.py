from fastapi import FastAPI

from data_base import BOOKS
from models import Book

app = FastAPI()


@app.get("/books")
async def get_books() -> list[Book]:
    return BOOKS
