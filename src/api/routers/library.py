from fastapi import APIRouter

from src.api.dependencies import (
    LibraryServiceDep,
    CurrentUserIdDep
)
from src.schemas.books import (
    SaveBookResponse,
    GetBooksResponse,
    UpdateBookRequest,
    UpdateBookResponse,
    DeleteBookResponse
)

router = APIRouter()


@router.get("/")
async def get_my_books(
    service: LibraryServiceDep,
    curr_user_id: CurrentUserIdDep
) -> GetBooksResponse:
    return await service.get_my_books(curr_user_id)


@router.post("/{book_id}", summary="Save book using id FROM /books/search/")
async def save_book(
    book_id: int,
    service: LibraryServiceDep,
    curr_user_id: CurrentUserIdDep
) -> SaveBookResponse:
    return await service.save_book(curr_user_id, book_id)


@router.put("/{book_id}/", summary="Update book using id FROM /library/")
async def update_book(
    book_id: str,
    payload: UpdateBookRequest,
    service: LibraryServiceDep,
    curr_user_id: CurrentUserIdDep
) -> UpdateBookResponse:
    return await service.update_book(curr_user_id, book_id, payload)


@router.delete("/{book_id}/", summary="Delete book using id FROM /library/")
async def delete_book(
    book_id: str,
    service: LibraryServiceDep,
    curr_user_id: CurrentUserIdDep
) -> DeleteBookResponse:
    return await service.delete_book(curr_user_id, book_id)
