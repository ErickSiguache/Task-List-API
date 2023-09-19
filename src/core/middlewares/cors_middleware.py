"""Configuration for the CORS middleware in the application"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Configure the allowed origins for CORS
origins = [
    "http://localhost",
    "http://localhost:5173",  # Example for a development React server
    "http://localhost:4200",  # Example for a development Angular server
]


def set_cors_configuration(app: FastAPI):
    """
    Function to configure the permissions for accessing the application
    from other services.

    Args:
        app (FastAPI): The instance of FastAPI to configure access.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "PATCH"],
        allow_headers=["*"],
    )
