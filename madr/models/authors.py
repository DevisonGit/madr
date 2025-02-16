from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

from .books import Book

table_registry = registry()


@table_registry.mapped_as_dataclass
class Author:
    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    books: Mapped[list['Book']] = relationship(
        init=False, back_populates='author', cascade='all, delete-orphan'
    )
