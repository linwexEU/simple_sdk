from fastapi import APIRouter

from src.schemas.books import SearchBooksResponse
from src.api.dependencies import BooksServiceDep

router = APIRouter()


@router.get("/search")
async def search_books(query: str, service: BooksServiceDep) -> SearchBooksResponse:
    """
        :param query: Example value query=books about wizards
    """
    return await service.search_books(query)
