from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    category: str

    class Config:
        extra = "forbid"  # Prohíbe campos adicionales
