from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

from .authors import Author

table_registry = registry()


@table_registry.mapped_as_dataclass
class Book:
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    year: Mapped[int]
    title: Mapped[str] = mapped_column(unique=True)
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'))
    author: Mapped[Author] = relationship(init=False, back_populates='books')
