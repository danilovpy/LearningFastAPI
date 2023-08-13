from sqlmodel import SQLModel, Field
from schemas.books import BookBase


# db model


class Book(BookBase, table=True):

    __tablename__ = "books"

    id: int = Field(default=None, nullable=False, primary_key=True)
