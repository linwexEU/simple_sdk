import uuid
from dataclasses import dataclass, field


@dataclass
class Book:
    id: str = field(default_factory=lambda: str(uuid.uuid4()), kw_only=True)
    title: str
    image: str | None
    author: str
    number_of_pages: int
