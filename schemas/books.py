from sqlmodel import SQLModel

# sqlmodel/pydantic schema


class BookBase(SQLModel):
    name: str
    description: str | None = None
    price: float


class BookCreate(BookBase):
    pass
