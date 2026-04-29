from typing import Annotated

from fastapi import Depends, Request, HTTPException, status

from src.api.services import (
    BooksService,
    LibraryService,
    UsersService
)
from src.core.interfaces.repositories import (
    AbstractUsersRepository,
    AbstractLibraryRepository
)
from src.core.database.db import db
from src.infrastructure.repositories import (
    UsersRepository,
    LibraryRepository
)

users_repo = UsersRepository(db)
library_repo = LibraryRepository(db)


def get_users_repo() -> UsersRepository:
    return users_repo


def get_library_repo() -> LibraryRepository:
    return library_repo


def get_users_service(
    request: Request,
    repo: AbstractUsersRepository = Depends(get_users_repo),
) -> UsersService:
    return UsersService(
        repo,
        request.app.state.email_verifier
    )


def get_library_service(
    request: Request,
    repo: AbstractLibraryRepository = Depends(get_library_repo),
) -> LibraryService:
    return LibraryService(
        repo,
        request.app.state.books_client
    )


def get_books_service(request: Request) -> BooksService:
    return BooksService(request.app.state.books_client)


def get_current_user_id(request: Request) -> str:
    user_id = request.cookies.get("auth_token")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user_id


UsersServiceDep = Annotated[UsersService, Depends(get_users_service)]
BooksServiceDep = Annotated[BooksService, Depends(get_books_service)]
LibraryServiceDep = Annotated[LibraryService, Depends(get_library_service)]
CurrentUserIdDep = Annotated[str, Depends(get_current_user_id)]
