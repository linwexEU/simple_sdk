from abc import ABC, abstractmethod
from typing import Any


class AbstractBookHttpClient(ABC):
    @abstractmethod
    async def search_books(self, query: str) -> dict[str, Any]:
        ...

    @abstractmethod
    async def get_book_info(self, book_id: int) -> dict[str, Any]:
        ...
