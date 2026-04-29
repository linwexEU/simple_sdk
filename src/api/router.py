from fastapi import APIRouter

from src.api.routers import users_router, books_router, library_router

router = APIRouter()

# Include all routers
router.include_router(users_router, prefix="/users", tags=["Users"])
router.include_router(books_router, prefix="/books", tags=["Books"])
router.include_router(library_router, prefix="/library", tags=["Library"])
