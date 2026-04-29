__all__ = (
    "BookAlreadyExistsError",
    "BookNotFoundError",
    "UserAlreadyExistsError",
    "UserNotFoundError"
)

from src.exceptions.repositories.library import (
    BookAlreadyExistsError,
    BookNotFoundError
)
from src.exceptions.repositories.users import (
    UserAlreadyExistsError,
    UserNotFoundError
)
