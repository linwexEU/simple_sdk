import logging

from fastapi import Depends

from src.exceptions.repositories import UserNotFoundError
from src.exceptions.repositories import UserAlreadyExistsError
from src.exceptions.services.users import UserAlreadyExistsServiceError, UserNotFoundServiceError
from src.exceptions.services import InvalidUserEmailError
from src.core.interfaces.email_verifiers import AbstractEmailVerifier
from src.core.interfaces.repositories import AbstractUsersRepository
from src.mappers.users import UserMapper
from src.schemas.users import (
    CreateUserRequest,
    CreateUserResponse,
    AuthUserRequest,
    AuthUserResponse
)

logger = logging.getLogger(__name__)


class UsersService:
    def __init__(
        self,
        repo: AbstractUsersRepository = Depends(),
        email_verifier: AbstractEmailVerifier = Depends(),
    ) -> None:
        self.repo = repo
        self.email_verifier = email_verifier

    async def register_user(self, payload: CreateUserRequest) -> CreateUserResponse:
        validation_result = await self.email_verifier.validate_email(payload.email)

        if validation_result["data"]["status"] == "invalid":
            raise InvalidUserEmailError(f"Invalid email '{payload.email}'")

        try:
            user = self.repo.create(UserMapper.to_entity(payload))
        except UserAlreadyExistsError as exc:
            logger.error(f"User with email '{payload.email}' already exists")
            raise UserAlreadyExistsServiceError(f"User with email '{payload.email}' already exists") from exc

        return CreateUserResponse(
            id=user.id,
            email=user.email,
        )

    def authenticate_user(self, payload: AuthUserRequest) -> AuthUserResponse:
        try:
            user = self.repo.select_by_email(payload.email)
        except UserNotFoundError as exc:
            logger.error(f"User with email '{payload.email}' not found")
            raise UserNotFoundServiceError(f"User with email '{payload.email}' not found") from exc
        return AuthUserResponse(user_id=user.id)
