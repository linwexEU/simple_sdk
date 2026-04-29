from abc import ABC, abstractmethod

from src.core.entities.books import Book


class AbstractLibraryRepository(ABC):
    @abstractmethod
    def save(self, user_id: str, book: Book) -> Book:
        ...

    @abstractmethod
    def select_all(self, user_id: str) -> list[Book]:
        ...

    @abstractmethod
    def update(
        self,
        user_id: str,
        book_id: str,
        title: str | None = None,
        image: str | None = None,
        author: str | None = None,
        number_of_pages: int | None = None
    ) -> Book:
        ...

    @abstractmethod
    def delete(self, user_id: str, book_id: str) -> None:
        ...
