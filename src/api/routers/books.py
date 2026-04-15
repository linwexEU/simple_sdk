from fastapi import APIRouter

from src.schemas.books import SBookUpdate
from src.schemas.books import ListBooks, SBook, SBookResponse
from src.api.depencencies import BooksServiceDep, CurrentUserDep

router = APIRouter()


@router.get("/")
async def get_books(service: BooksServiceDep) -> ListBooks:
    return service.get_books()


@router.post("/")
async def create_book(
    book: SBook,
    service: BooksServiceDep,
    _: CurrentUserDep
) -> SBookResponse:
    return service.create_book(book)


@router.put("/{book_uuid}")
async def update_book(
    book_uuid: str,
    book: SBookUpdate,
    service: BooksServiceDep,
    _: CurrentUserDep
) -> SBookResponse:
    return service.update_book(book_uuid, book)


@router.delete("/{book_uuid}")
async def delete_book(
    book_uuid: str,
    service: BooksServiceDep,
    _: CurrentUserDep
) -> SBookResponse:
    return service.delete_book(book_uuid)
