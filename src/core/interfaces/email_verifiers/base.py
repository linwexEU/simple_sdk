from abc import ABC, abstractmethod
from typing import Any


class AbstractEmailVerifier(ABC):
    @abstractmethod
    async def validate_email(self, email: str) -> dict[str, Any]:
        ...
