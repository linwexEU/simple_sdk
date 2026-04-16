import asyncio
from functools import wraps
import logging
from typing import Any, Callable

import aiohttp
from fastapi import status

from src.exceptions.http.http_exception import ExternalAPIException
from src.utils.config import settings

logger = logging.getLogger(__name__)


async def _execute_with_retry(
    func: Callable[..., Any],
    attempts: int
) -> Any:
    last_exception = None

    for attempt in range(1, attempts + 1):
        try:
            return await func()  # noqa: WPS476
        except (aiohttp.ClientError, asyncio.TimeoutError) as ex:
            last_exception = ex
            logger.warning(f"Attempt {attempt}/{attempts} failed: {ex}")

        if attempt < attempts:
            await asyncio.sleep(2 ** attempt)  # noqa: WPS476

    raise ExternalAPIException from last_exception


def retry(attempts: int):
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            return await _execute_with_retry(lambda: func(*args, **kwargs), attempts)
        return wrapper
    return decorator


class HttpClient:
    """Client to work with external API"""
    def __init__(self) -> None:
        self.session: aiohttp.ClientSession = aiohttp.ClientSession()

    @retry(5)
    async def validate_email(self, email: str) -> dict[str, Any]:
        query_params = {
            "email": email,
            "api_key": settings.API_KEY
        }
        async with self.session.get("https://api.hunter.io/v2/email-verifier", params=query_params) as response:
            if response.status != status.HTTP_200_OK:
                raise ExternalAPIException(f"Bad status: {response.status}")

            json = await response.json()
            return json
