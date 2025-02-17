
from typing import Optional

from pydantic import BaseModel, Field


class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int


class BookRequest(BaseModel):
    id: Optional[int] = None 
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, le=5)
    published_date: int

    class Config:
        extra = "forbid"  # Prohíbe campos adicionales
