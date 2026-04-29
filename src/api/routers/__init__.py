__all__ = (
    "users_router",
    "books_router",
    "library_router"
)

from src.api.routers.users import router as users_router
from src.api.routers.books import router as books_router
from src.api.routers.library import router as library_router
