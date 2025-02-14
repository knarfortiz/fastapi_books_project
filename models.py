
from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    class Config:
        extra = "forbid"  # Prohíbe campos adicionales
