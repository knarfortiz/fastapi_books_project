from fastapi import HTTPException

from data_base import BOOKS


def validate_book_id(id: int) -> int:
    if id not in BOOKS:
        raise HTTPException(status_code=404, detail="Book not found")
    return id