from pydantic import BaseModel


class BookSchema(BaseModel):
    title: str
    year: int
    author_id: int


class BookPublic(BookSchema):
    id: int
