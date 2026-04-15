from typing import Literal

from pydantic import BaseModel


class SAuth(BaseModel):
    email: str
    status: Literal["valid", "invalid"] = "valid"
