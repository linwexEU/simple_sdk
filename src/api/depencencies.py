from typing import Annotated

from fastapi import Depends, Request, HTTPException, status

from src.repositories.books import InMemoryBookRepository
from src.repositories.base import AbstractRepository
from src.api.services.books import BooksService
from src.api.services.auth import AuthService

books_repo = InMemoryBookRepository()


def get_books_repo() -> InMemoryBookRepository:
    """Return InMemoryBookRepository"""
    return books_repo


def get_books_service(repo: type[AbstractRepository] = Depends(get_books_repo)) -> BooksService:
    """Function for getting Books Service with dependencies"""
    return BooksService(repo)


def get_auth_service(request: Request) -> AuthService:
    """Function for getting Auth Service with dependencies"""
    return AuthService(request.app.state.http_client)


def get_current_user(request: Request) -> None:
    """Return current user base on cookie"""
    token = request.cookies.get("auth")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


BooksServiceDep = Annotated[BooksService, Depends(get_books_service)]
AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]
CurrentUserDep = Annotated[None, Depends(get_current_user)]
