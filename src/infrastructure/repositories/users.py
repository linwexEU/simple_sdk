from src.exceptions.repositories.users import UserAlreadyExistsError, UserNotFoundError
from src.core.entities.users import User
from src.core.database.db import InMemoryDb
from src.core.interfaces.repositories import AbstractUsersRepository


class UsersRepository(AbstractUsersRepository):
    def __init__(self, db: InMemoryDb) -> None:
        self.users = db.users
        self.library = db.library

    def create(self, user: User) -> User:
        for db_user in self.users:
            if db_user.email == user.email:
                raise UserAlreadyExistsError
        self.users.append(user)
        self.library[user.id] = []
        return user

    def select_by_email(self, email: str) -> User:
        for db_user in self.users:
            if db_user.email == email:
                return db_user

        raise UserNotFoundError
