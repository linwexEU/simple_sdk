import logging

from fastapi import Depends

from src.exceptions.repositories import (
    BookNotFoundError,
    BookAlreadyExistsError,
    UserNotFoundError
)
from src.exceptions.services import (
    UserNotFoundServiceError,
    BookAlreadyExistsServiceError,
    BookNotFoundServiceError
)
from src.schemas.books import (
    SaveBookResponse,
    GetBooksResponse,
    UpdateBookRequest,
    UpdateBookResponse, DeleteBookResponse
)
from src.core.entities import Book
from src.core.interfaces.http_clients import AbstractBookHttpClient
from src.core.interfaces.repositories import AbstractLibraryRepository

logger = logging.getLogger(__name__)


class LibraryService:
    def __init__(
        self,
        repo: AbstractLibraryRepository = Depends(),
        books_client: AbstractBookHttpClient = Depends()
    ) -> None:
        self.repo = repo
        self.books_client = books_client

    async def get_my_books(self, user_id: str) -> GetBooksResponse:
        try:
            books = self.repo.select_all(user_id)
        except UserNotFoundError as exc:
            logger.error(
                f"User with id '{user_id}' not found",
                extra={"user_id": user_id}
            )
            raise UserNotFoundServiceError(f"User with id '{user_id}' not found") from exc
        return GetBooksResponse.build(books)

    async def save_book(self, user_id: str, book_id: int) -> SaveBookResponse:
        book_info = await self.books_client.get_book_info(book_id)

        if len(book_info["authors"]) > 0:
            author = book_info["authors"][0]["name"]
        else:
            author = "Unknown"

        book = Book(
            title=book_info["title"],
            image=book_info.get("image"),
            author=author,
            number_of_pages=book_info.get("number_of_pages", 0),
        )
        try:
            self.repo.save(user_id, book)
        except UserNotFoundError as exc:
            logger.error(
                f"User with id '{user_id}' not found",
                extra={"user_id": user_id}
            )
            raise UserNotFoundServiceError(f"User with id '{user_id}' not found") from exc
        except BookAlreadyExistsError as exc:
            logger.error(
                f"Book with id '{book_id}' already exists",
                extra={
                    "book_id": book_id
                }
            )
            raise BookAlreadyExistsServiceError(f"Book with id '{book_id} already saved'") from exc
        return SaveBookResponse.build(book)

    async def update_book(
        self,
        user_id: str,
        book_id: str,
        payload: UpdateBookRequest
    ) -> UpdateBookResponse:
        try:
            book = self.repo.update(user_id, book_id, **payload.model_dump())
        except UserNotFoundError as exc:
            logger.error(
                f"User with id '{user_id}' not found",
                extra={"user_id": user_id}
            )
            raise UserNotFoundServiceError(f"User with id '{user_id}' not found") from exc
        except BookNotFoundError as exc:
            logger.error(
                f"Book with id '{book_id}' not found",
                extra={
                    "book_id": book_id
                }
            )
            raise BookNotFoundServiceError(f"Book with id '{book_id}' not found") from exc
        return UpdateBookResponse(book_id=book.id)

    async def delete_book(self, user_id: str, book_id: str) -> DeleteBookResponse:
        try:
            self.repo.delete(user_id, book_id)
        except UserNotFoundError as exc:
            logger.error(
                f"User with id '{user_id}' not found",
                extra={"user_id": user_id}
            )
            raise UserNotFoundServiceError(f"User with id '{user_id}' not found") from exc
        except BookNotFoundError as exc:
            logger.error(
                f"Book with id '{book_id}' not found",
                extra={
                    "book_id": book_id
                }
            )
            raise BookNotFoundServiceError(f"Book with id '{book_id}' not found") from exc
        return DeleteBookResponse(book_id=book_id)
