from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import FastAPI

from src.exceptions.handlers.books import book_not_found_handler
from src.exceptions.handlers.http_exception import external_api_error_handler
from src.exceptions.services.books import BookNotFoundServiceException
from src.exceptions.http.http_exception import ExternalAPIException
from src.api import router as main_router
from src.utils.logger import config_logger
from src.utils.http_client import HttpClient


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    config_logger()
    app.state.http_client = HttpClient()
    yield
    await app.state.http_client.session.close()


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    # Include all routers
    app.include_router(main_router)

    # Add all exception handlers
    app.add_exception_handler(BookNotFoundServiceException, book_not_found_handler)
    app.add_exception_handler(ExternalAPIException, external_api_error_handler)

    return app


app = create_app()
