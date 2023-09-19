"""The test to check if the application is running"""
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse


health_route = APIRouter(prefix="/health", tags=["Health"])


@health_route.get("/", response_model=str, status_code=200)
def get_health() -> JSONResponse:
    """
    This method is only a test to check if the application is running

    Returns:
        JSONResponse: The JSON response that represents that the
        application is running.
    """
    return JSONResponse(
        content={
            "status": "success",
            "message": "The application is running",
        },
        status_code=status.HTTP_200_OK,
    )
