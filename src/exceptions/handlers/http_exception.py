from fastapi import Request, status
from fastapi.responses import JSONResponse

from src.exceptions.http.http_exception import ExternalAPIException


async def external_api_error_handler(request: Request, exc: ExternalAPIException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": "EXTERNAL_API_EXCEPTION",
            "message": f"External API Error: {str(exc)}",
        },
    )
