import uuid
from typing import Any

from src.repositories.base import AbstractRepository
from src.exceptions.repositories.books import BookNotFoundException


class InMemoryBookRepository(AbstractRepository):
    """InMemoryRepository with all crud operations"""
    def __init__(self) -> None:
        self.books = []

    def get_all(self) -> list[dict[str, Any]]:
        return self.books

    def create(self, title: str, author: str, price: float) -> str:
        book_uuid = str(uuid.uuid4())
        self.books.append(
            {
                "book_uuid": book_uuid,
                "title": title,
                "author": author,
                "price": price
            }
        )
        return book_uuid

    def delete(self, book_uuid: str) -> str:
        for book in self.books:
            if book["book_uuid"] == book_uuid:
                self.books.remove(book)
                return book_uuid

        raise BookNotFoundException

    def update(
        self,
        book_uuid: str,
        title: str | None = None,
        author: str | None = None,
        price: float | None = None
    ) -> str:
        book_to_update = None
        for book in self.books:
            if book["book_uuid"] == book_uuid:
                book_to_update = book

        if book_to_update:
            book_to_update["title"] = title or book_to_update["title"]
            book_to_update["author"] = author or book_to_update["author"]
            book_to_update["price"] = price or book_to_update["price"]
        else:
            raise BookNotFoundException

        return book_uuid
