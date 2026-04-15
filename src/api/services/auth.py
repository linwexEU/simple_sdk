from src.utils.http_client import HttpClient


class AuthService:
    """Auth Service with email validation"""
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    async def authenticate(self, email: str) -> bool:
        response = await self.http_client.validate_email(email)
        if response["data"]["status"] == "valid":
            return True
        return False
