from src.core.entities.users import User
from src.schemas.users import CreateUserRequest


class UserMapper:
    @staticmethod
    def to_entity(schema: CreateUserRequest) -> User:
        return User(
            email=schema.email,
        )
