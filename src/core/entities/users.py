import uuid
from dataclasses import dataclass, field


@dataclass
class User:
    id: str = field(default_factory=lambda: str(uuid.uuid4()), kw_only=True)
    email: str
