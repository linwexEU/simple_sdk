from src.core.entities import User, Book


class InMemoryDb:
    def __init__(self) -> None:
        self._users: list[User] = []
        self._library: dict[str, list[Book]] = {}

    @property
    def users(self) -> list[User]:
        return self._users

    @property
    def library(self) -> dict[str, list[Book]]:
        return self._library


db = InMemoryDb()
