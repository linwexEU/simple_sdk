from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import FastAPI

from src.exceptions.http import ExternalAPIException
from src.api.router import router as main_router
from src.core.logger import config_logger
from src.infrastructure.email_verifiers.hunter import HunterEmailVerifier
from src.infrastructure.http_clients.books import BigBookHttpClient
from src.exceptions.services import (
    InvalidUserEmailError,
    UserAlreadyExistsServiceError,
    UserNotFoundServiceError,
    BookNotFoundServiceError,
    BookAlreadyExistsServiceError
)
from src.exceptions.handlers import (
    invalid_user_email_error_handler,
    user_already_exists_error_handler,
    user_not_found_error_handler,
    external_api_error_handler,
    book_not_found_error_handler,
    book_already_exists_error_handler
)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    config_logger()
    app.state.email_verifier = HunterEmailVerifier()
    app.state.books_client = BigBookHttpClient()
    yield
    await app.state.email_verifier.session.close()
    await app.state.books_client.session.close()


def _add_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        InvalidUserEmailError,
        invalid_user_email_error_handler
    )
    app.add_exception_handler(
        UserAlreadyExistsServiceError,
        user_already_exists_error_handler
    )
    app.add_exception_handler(
        UserNotFoundServiceError,
        user_not_found_error_handler
    )
    app.add_exception_handler(
        ExternalAPIException,
        external_api_error_handler
    )
    app.add_exception_handler(
        BookNotFoundServiceError,
        book_not_found_error_handler
    )
    app.add_exception_handler(
        BookAlreadyExistsServiceError,
        book_already_exists_error_handler
    )


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    # Include all routers
    app.include_router(main_router)

    # Add all exception handlers
    _add_exception_handlers(app)

    return app


app = create_app()
