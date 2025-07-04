from pydantic import BaseModel

from src.madr.shared.schema import FilterPage


class BookBase(BaseModel):
    year: int
    title: str
    author_id: int


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    year: int | None = None
    title: str | None = None
    author_id: int | None = None


class BookPublic(BookBase):
    id: int


class BookFilter(FilterPage):
    year: int | None = None
    title: str | None = None


class BookList(BaseModel):
    books: list[BookPublic]
