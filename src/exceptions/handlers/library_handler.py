from fastapi import Request, status
from fastapi.responses import JSONResponse

from src.exceptions.services.library import BookNotFoundServiceError, BookAlreadyExistsServiceError


async def book_not_found_error_handler(
    request: Request,
    exc: BookNotFoundServiceError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "BOOK_NOT_FOUND",
            "message": str(exc),
        },
    )


async def book_already_exists_error_handler(
    request: Request,
    exc: BookAlreadyExistsServiceError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "error": "BOOK_ALREADY_EXISTS",
            "message": str(exc),
        },
    )
