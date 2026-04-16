from fastapi import APIRouter

from src.api.routers import auth_router, books_router

router = APIRouter()

# Include all routers
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(books_router, prefix="/books", tags=["Books"])
