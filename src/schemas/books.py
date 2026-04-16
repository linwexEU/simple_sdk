from typing import Any

from pydantic import BaseModel


class SBook(BaseModel):
    title: str
    author: str
    price: float

    @classmethod
    def build(cls, book: dict[str, Any]) -> "SBook":
        return cls(**book)


class SFullBook(SBook):
    book_uuid: str

    @classmethod
    def build(cls, book: dict[str, Any]) -> "SFullBook":
        return cls(**book)


class SBookResponse(BaseModel):
    book_uuid: str

    @classmethod
    def build(cls, book_uuid: str) -> "SBookResponse":
        return cls(book_uuid=book_uuid)


class ListBooks(BaseModel):
    books: list[SFullBook]

    @classmethod
    def build(cls, books: list[dict[str, Any]]) -> "ListBooks":
        schema_books = [SFullBook.build(book) for book in books]
        return cls(books=schema_books)


class SBookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    price: float | None = None
