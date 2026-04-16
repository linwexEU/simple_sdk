from typing import Annotated

from fastapi import APIRouter, Body, Response
from pydantic import EmailStr

from src.schemas.auth_schema import SAuth
from src.api.depencencies import AuthServiceDep
from src.utils.config import settings

router = APIRouter()


@router.post("/")
async def authentication(
    response: Response,
    email: Annotated[EmailStr, Body(embed=True)],
    service: AuthServiceDep
) -> SAuth:
    valid = await service.authenticate(email)
    if valid:
        response.set_cookie(
            "auth",
            email,
            max_age=settings.COOKIE_MAX_AGE,
            secure=True,
            httponly=True,
            samesite="lax"
        )
        return SAuth(email=email, status="valid")
    return SAuth(email=email, status="invalid")
