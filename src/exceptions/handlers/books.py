from fastapi import Request, status
from fastapi.responses import JSONResponse

from src.exceptions.services.books import BookNotFoundServiceException


async def book_not_found_handler(request: Request, exc: BookNotFoundServiceException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "BOOK_NOT_FOUND",
            "message": f"Book {exc.book_uuid} not found",
        },
    )
