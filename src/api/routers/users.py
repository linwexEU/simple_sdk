from fastapi import APIRouter, Response

from src.schemas.users import (
    CreateUserRequest,
    CreateUserResponse,
    AuthUserRequest,
    AuthUserResponse,
)
from src.api.dependencies import UsersServiceDep

router = APIRouter()


@router.post("/register")
async def register_user(
    payload: CreateUserRequest,
    service: UsersServiceDep
) -> CreateUserResponse:
    return await service.register_user(payload)


@router.post("/auth")
async def authenticate_user(
    response: Response,
    payload: AuthUserRequest,
    service: UsersServiceDep
) -> AuthUserResponse:
    user_info = service.authenticate_user(payload)

    response.set_cookie(
        key="auth_token",
        value=user_info.user_id,
        httponly=True,
        samesite="lax",
    )

    return user_info
