from abc import ABC, abstractmethod

from src.core.entities.users import User


class AbstractUsersRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        ...

    @abstractmethod
    def select_by_email(self, email: str) -> User:
        ...
