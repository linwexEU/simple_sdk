import asyncio
from functools import wraps
import logging
from typing import Any, Callable

import aiohttp

from src.exceptions.http.http_exception import ExternalAPIException
from src.utils.config import settings

logger = logging.getLogger(__name__)


def retry(attempts: int):
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None

            for attempt in range(1, attempts + 1):
                try:
                    return await func(*args, **kwargs)
                except (aiohttp.ClientError, aiohttp.ClientTimeout, asyncio.TimeoutError) as ex:
                    last_exception = ex
                    logger.warning(f"Attempt {attempt}/{attempts} failed: {ex}")

                if attempt < attempts:
                    await asyncio.sleep(2 ** attempt)

            raise ExternalAPIException from last_exception

        return wrapper
    return decorator


class HttpClient:
    """Client to work with external API"""
    def __init__(self) -> None:
        self.session: aiohttp.ClientSession = aiohttp.ClientSession()

    @retry(5)
    async def validate_email(self, email: str) -> dict[str, Any]:
        params = {
            "email": email,
            "api_key": settings.API_KEY
        }
        async with self.session.get("https://api.hunter.io/v2/email-verifier", params=params) as response:
            if response.status != 200:
                raise ExternalAPIException(f"Bad status: {response.status}")

            data = await response.json()
            return data
