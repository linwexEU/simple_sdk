from abc import ABC, abstractmethod
from typing import Any


class AbstractRepository(ABC):
    @abstractmethod
    def get_all(self) -> Any:
        ...

    @abstractmethod
    def create(self, *args: Any, **kwargs: Any) -> Any:
        ...

    @abstractmethod
    def delete(self, *args: Any, **kwargs: Any) -> Any:
        ...

    @abstractmethod
    def update(self, *args: Any, **kwargs: Any) -> Any:
        ...
