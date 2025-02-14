from models import Book

BOOKS: list[Book] = [
    Book(id=1, title="Computer Science Pro", author="codingwithroby", description="A very nice book!", rating=5, published_date=2030),
    Book(id=2, title="Be Fast with FastAPI", author="codingwithroby", description="A great book!", rating=5, published_date=2030),
    Book(id=3, title="Master Endpoints", author="codingwithroby", description="An awesome book!", rating=5, published_date=2029),
    Book(id=4, title="HP1", author="Author 1", description="Book Description", rating=2, published_date=2028),
    Book(id=5, title="HP2", author="Author 2", description="Book Description", rating=3, published_date=2027),
    Book(id=6, title="HP3", author="Author 3", description="Book Description", rating=1, published_date=2026),
]