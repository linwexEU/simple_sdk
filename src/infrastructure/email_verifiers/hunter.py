import logging
from typing import Any

import aiohttp
from fastapi import status

from src.core.interfaces.email_verifiers.base import AbstractEmailVerifier
from src.infrastructure.http_utils.helper import retry
from src.core.config import settings
from src.exceptions.http import ExternalAPIException

logger = logging.getLogger(__name__)


class HunterEmailVerifier(AbstractEmailVerifier):
    """Client to verify email with Hunter API"""
    def __init__(self) -> None:
        self.session: aiohttp.ClientSession = aiohttp.ClientSession()

    @retry(5)
    async def validate_email(self, email: str) -> dict[str, Any]:
        query_params = {
            "email": email,
            "api_key": settings.HUNTER_API_KEY
        }
        async with self.session.get("https://api.hunter.io/v2/email-verifier", params=query_params) as response:
            if response.status != status.HTTP_200_OK:
                logger.error(f"Bad response from Hunter API: {response.status}")
                raise ExternalAPIException(f"Bad status: {response.status}")

            json = await response.json()
            return json
