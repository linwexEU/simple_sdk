__all__ = (
    "auth_router",
    "books_router"
)

from src.api.routers.auth_router import router as auth_router
from src.api.routers.books_router import router as books_router
