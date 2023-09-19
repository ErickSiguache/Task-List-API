"""The point of intersection between all routes of the application"""
from typing import Final
from fastapi import FastAPI
from src.core.routes.health_routes import health_route
from src.modules.categories.controllers.category_controller import category_route

PREFIX_PATH: Final[str] = "/api/v1/"


def load_routes(app: FastAPI) -> None:
    """
    Function to load routes from the controllers to set up the
    principal routes of the API.

    Args:
        app (FastAPI): An instance of FastAPI
    """
    app.include_router(health_route, prefix="")
    app.include_router(category_route, prefix="")
