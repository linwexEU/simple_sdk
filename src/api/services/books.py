from fastapi import Depends

from src.core.interfaces.http_clients import AbstractBookHttpClient
from src.schemas.books import SearchBooksResponse


class BooksService:
    def __init__(
        self,
        books_client: AbstractBookHttpClient = Depends()
    ) -> None:
        self.books_client = books_client

    async def search_books(self, query: str) -> SearchBooksResponse:
        books = await self.books_client.search_books(query)
        return SearchBooksResponse.build(books)
