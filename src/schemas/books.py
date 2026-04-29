from typing import Any

from pydantic import BaseModel

from src.core.entities import Book


class SearchedBook(BaseModel):
    id: int
    title: str
    image: str | None
    author: str


class SearchBooksResponse(BaseModel):
    books: list[SearchedBook]

    @classmethod
    def build(cls, searched_books: dict[str, Any]) -> "SearchBooksResponse":
        resulted_books = []
        for books in searched_books["books"]:
            for book in books:
                if len(book["authors"]) > 0:
                    author = book["authors"][0]["name"]
                else:
                    author = "Unknown"

                resulted_books.append(
                    SearchedBook(
                        id=book["id"],
                        title=book.get("title"),
                        image=book.get("image"),
                        author=author
                    )
                )
        return cls(books=resulted_books)


class SaveBookResponse(BaseModel):
    book_id: str

    @classmethod
    def build(cls, book: Book) -> "SaveBookResponse":
        return SaveBookResponse(
            book_id=book.id
        )


class UpdateBookRequest(BaseModel):
    title: str | None = None
    image: str | None = None
    author: str | None = None
    number_of_pages: int | None = None


class UpdateBookResponse(BaseModel):
    book_id: str


class DeleteBookResponse(UpdateBookResponse):
    """Same as UpdateBookResponse, but with book id removed"""


class MyBook(SaveBookResponse):
    title: str
    image: str | None
    author: str
    number_of_pages: int

    @classmethod
    def build(cls, book: Book) -> "MyBook":
        return MyBook(
            book_id=book.id,
            title=book.title,
            image=book.image,
            author=book.author,
            number_of_pages=book.number_of_pages
        )


class GetBooksResponse(BaseModel):
    books: list[MyBook]

    @classmethod
    def build(cls, books: list[Book]) -> "GetBooksResponse":
        resulted_books = []
        for book in books:
            resulted_books.append(MyBook.build(book))
        return cls(books=resulted_books)
