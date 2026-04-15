from fastapi import APIRouter

from src.api.routers.books import router as books_router
from src.api.routers.auth import router as auth_router

router = APIRouter()

# Include all routers
router.include_router(auth_router, prefix="/auth", tags=["Auth"])

router.include_router(books_router, prefix="/books", tags=["Books"])
