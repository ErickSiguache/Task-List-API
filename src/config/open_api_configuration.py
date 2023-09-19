"""Configuration for the application documentation"""
from fastapi import FastAPI


def create_app() -> FastAPI:
    """
    Function to create a FastAPI instance and configure it with the
    OpenAPI documentation settings.

    Returns:
        FastAPI: An instance of FastAPI to run the application.
    """
    return FastAPI(
        docs_url="/api/docs",
        redoc_url="/api/redocs",
        title="Task List API",
        description="The task list API documentation",
        version="1.0",
        openapi_url="/api/openapi.json",
    )
