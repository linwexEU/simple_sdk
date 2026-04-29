from fastapi import Request, status
from fastapi.responses import JSONResponse

from src.exceptions.services.users import (
    UserAlreadyExistsServiceError,
    InvalidUserEmailError,
    UserNotFoundServiceError
)


async def user_already_exists_error_handler(
    request: Request,
    exc: UserAlreadyExistsServiceError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "error": "USER_ALREADY_EXISTS_ERROR",
            "message": str(exc),
        },
    )


async def invalid_user_email_error_handler(
    request: Request,
    exc: InvalidUserEmailError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": "INVALID_USER_EMAIL_ERROR",
            "message": str(exc),
        },
    )


async def user_not_found_error_handler(
    request: Request,
    exc: UserNotFoundServiceError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "USER_NOT_FOUND_ERROR",
            "message": str(exc),
        },
    )
