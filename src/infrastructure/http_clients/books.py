import logging
from typing import Any

import aiohttp
from fastapi import status

from src.exceptions.http import ExternalAPIException
from src.core.interfaces.http_clients.books import AbstractBookHttpClient
from src.core.config import settings

logger = logging.getLogger(__name__)


class BigBookHttpClient(AbstractBookHttpClient):
    """Client to work with Big Book API"""
    def __init__(self) -> None:
        self.session: aiohttp.ClientSession = aiohttp.ClientSession()

    async def search_books(self, query: str) -> dict[str, Any]:
        query_params = {
            "query": query,
            "api-key": settings.BIG_BOOK_API_KEY
        }
        async with self.session.get(
            "https://api.bigbookapi.com/search-books",
            params=query_params
        ) as response:
            if response.status != status.HTTP_200_OK:
                logger.error(f"Bad status: {response.status}")
                raise ExternalAPIException(f"Bad status: {response.status}")

            json = await response.json()
            return json

    async def get_book_info(self, book_id: int) -> dict[str, Any]:
        query_params = {
            "api-key": settings.BIG_BOOK_API_KEY
        }
        async with self.session.get(
            f"https://api.bigbookapi.com/{book_id}",
            params=query_params
        ) as response:
            if response.status != status.HTTP_200_OK:
                logger.error(f"Bad status: {response.status}")
                raise ExternalAPIException(f"Bad status: {response.status}")

            json = await response.json()

            return json
