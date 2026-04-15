from typing import Any

from pydantic import BaseModel


class SBook(BaseModel):
    title: str
    author: str
    price: float

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "author": self.author,
            "price": self.price,
        }

    @staticmethod
    def build(book: dict[str, Any]) -> "SBook":
        return SBook(**book)


class SFullBook(SBook):
    book_uuid: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "book_uuid": self.book_uuid,
            "title": self.title,
            "author": self.author,
            "price": self.price,
        }

    @staticmethod
    def build(book: dict[str, Any]) -> "SFullBook":
        return SFullBook(**book)


class SBookResponse(BaseModel):
    book_uuid: str

    @staticmethod
    def build(book_uuid: str) -> "SBookResponse":
        return SBookResponse(book_uuid=book_uuid)


class ListBooks(BaseModel):
    books: list[SFullBook]

    @staticmethod
    def build(books: list[dict[str, Any]]) -> "ListBooks":
        schema_books = [SFullBook.build(book) for book in books]
        return ListBooks(books=schema_books)


class SBookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    price: float | None = None
