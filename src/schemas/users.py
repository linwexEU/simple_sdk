from pydantic import BaseModel, EmailStr


class CreateUserRequest(BaseModel):
    email: EmailStr


class CreateUserResponse(BaseModel):
    id: str
    email: EmailStr


class AuthUserRequest(CreateUserRequest):
    """Same as CreateUserRequest"""


class AuthUserResponse(BaseModel):
    user_id: str
