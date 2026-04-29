import asyncio
from functools import wraps
import logging
from typing import Any, Callable

import aiohttp

from src.exceptions.http import ExternalAPIException

logger = logging.getLogger(__name__)


async def _execute_with_retry(
    func: Callable[..., Any],
    attempts: int
) -> Any:
    last_exception = None

    for attempt in range(1, attempts + 1):
        try:
            return await func()
        except (aiohttp.ClientError, asyncio.TimeoutError) as ex:
            last_exception = ex
            logger.warning(f"Attempt {attempt}/{attempts} failed: {ex}")

        if attempt < attempts:
            await asyncio.sleep(2 ** attempt)

    raise ExternalAPIException from last_exception


def retry(attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            return await _execute_with_retry(lambda: func(*args, **kwargs), attempts)
        return wrapper
    return decorator
