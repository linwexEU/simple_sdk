from typing import Annotated

from fastapi import Depends, Request, HTTPException, status

from src.repositories import InMemoryBookRepository
from src.repositories import AbstractRepository
from src.api.services import BooksService, AuthService

books_repo = InMemoryBookRepository()


def get_books_repo() -> InMemoryBookRepository:
    """Return InMemoryBookRepository"""
    return books_repo


def get_books_service(
    repo: type[AbstractRepository] = Depends(get_books_repo)
) -> BooksService:
    """Function for getting Books Service with dependencies"""
    return BooksService(repo)


def get_auth_service(request: Request) -> AuthService:
    """Function for getting Auth Service with dependencies"""
    return AuthService(request.app.state.http_client)


def check_current_user(request: Request) -> None:
    """Return current user base on cookie"""
    token = request.cookies.get("auth")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


BooksServiceDep = Annotated[BooksService, Depends(get_books_service)]
AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]
CurrentUserDep = Annotated[None, Depends(check_current_user)]
