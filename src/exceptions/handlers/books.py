from fastapi import Request
from fastapi.responses import JSONResponse

from src.exceptions.services.books import BookNotFoundServiceException


async def book_not_found_handler(request: Request, exc: BookNotFoundServiceException):
    return JSONResponse(
        status_code=404,
        content={
            "error": "BOOK_NOT_FOUND",
            "message": f"Book {exc.book_uuid} not found",
        },
    )
