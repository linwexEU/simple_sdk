from src.exceptions.repositories import UserNotFoundError
from src.exceptions.repositories.library import BookAlreadyExistsError, BookNotFoundError
from src.core.entities import Book
from src.core.database.db import InMemoryDb
from src.core.interfaces.repositories import AbstractLibraryRepository


class LibraryRepository(AbstractLibraryRepository):
    def __init__(self, db: InMemoryDb) -> None:
        self.library = db.library

    def save(self, user_id: str, book: Book) -> Book:
        if user_id not in self.library:
            raise UserNotFoundError

        for db_book in self.library[user_id]:
            if db_book.title == book.title:
                raise BookAlreadyExistsError
        self.library[user_id].append(book)
        return book

    def select_all(self, user_id: str) -> list[Book]:
        if user_id not in self.library:
            raise UserNotFoundError

        return self.library[user_id]

    def update(
        self,
        user_id: str,
        book_id: str,
        title: str | None = None,
        image: str | None = None,
        author: str | None = None,
        number_of_pages: int | None = None
    ) -> Book:
        if user_id not in self.library:
            raise UserNotFoundError

        db_book = None
        for idx, book in enumerate(self.library[user_id]):
            if book.id == book_id:
                db_book = self.library[user_id][idx]

        if db_book is None:
            raise BookNotFoundError

        db_book.title = title or db_book.title
        db_book.image = image or db_book.image
        db_book.author = author or db_book.author
        db_book.number_of_pages = number_of_pages or db_book.number_of_pages

        return db_book

    def delete(self, user_id: str, book_id: str) -> None:
        if user_id not in self.library:
            raise UserNotFoundError

        for idx, book in enumerate(self.library[user_id]):
            if book.id == book_id:
                del self.library[user_id][idx]
                return

        raise BookNotFoundError
