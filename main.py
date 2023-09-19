"""Entry point of the application"""
from uvicorn import run
from src.config.open_api_configuration import create_app
from src.core.middlewares.cors_middleware import set_cors_configuration
from src.core.routes.application_routes import load_routes
from src.database.migrations.general_migrations import initialize_database


# Initialize the database (create tables)
initialize_database()


# Confuration of the server and routes
app = create_app()
set_cors_configuration(app)
load_routes(app)


if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8000, reload=True)
