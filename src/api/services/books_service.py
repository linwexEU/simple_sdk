import logging

from fastapi import Depends

from src.repositories import AbstractRepository
from src.exceptions import BookNotFoundException, BookNotFoundServiceException
from src.schemas import SBook, SBookUpdate, ListBooks, SBookResponse

logger = logging.getLogger(__name__)


class BooksService:
    """Books Service with all crud operations"""
    def __init__(
        self,
        repo: type[AbstractRepository] = Depends()  # noqa: WPS404
    ) -> None:
        self.repo = repo

    def get_books(self) -> ListBooks:
        return ListBooks.build(books=self.repo.get_all())

    def create_book(self, book: SBook) -> SBookResponse:
        book_uuid = self.repo.create(book.title, book.author, book.price)
        return SBookResponse.build(book_uuid=book_uuid)

    def update_book(self, book_uuid: str, book: SBookUpdate) -> SBookResponse:
        try:
            book_uuid = self.repo.update(book_uuid, book.title, book.author, book.price)
        except BookNotFoundException as ex:
            logger.warning(
                "Book not found while updating",
                extra={
                    "book_uuid": book_uuid,
                    "title": book.title,
                    "author": book.author,
                },
            )
            raise BookNotFoundServiceException(book_uuid) from ex
        return SBookResponse.build(book_uuid=book_uuid)

    def delete_book(self, book_uuid: str) -> SBookResponse:
        try:
            book_uuid = self.repo.delete(book_uuid)
        except BookNotFoundException as ex:
            logger.warning(
                "Book not found while deleting",
                extra={
                    "book_uuid": book_uuid
                },
            )
            raise BookNotFoundServiceException(book_uuid) from ex
        return SBookResponse.build(book_uuid=book_uuid)
