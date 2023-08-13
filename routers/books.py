from fastapi import APIRouter, status, Depends
# from schemas import books
from services.db import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from models.books import Book
from schemas.books import BookBase, BookCreate

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list[BookBase])
async def get_books(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Book))
    books = result.scalars().all()
    return books


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BookBase)
async def create_book(book: BookCreate, session: AsyncSession = Depends(get_session)):
    book = Book(name=book.name, description=book.description, price=book.price)
    session.add(book)
    await session.commit()
    await session.refresh(book)
    return book
