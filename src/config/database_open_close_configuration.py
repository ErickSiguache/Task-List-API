""" Configuration for open and close connections to the database """
from contextlib import contextmanager
from src.config.database_configuration import LocalSession


@contextmanager
def get_db():
    """Provicional para cerrar conexion"""
    db_session = LocalSession()
    try:
        print("The connection to the database is opening 🤞 😬 😬")
        yield db_session
    finally:
        print("The connection to the database was closed 😊 👌 ✔")
        db_session.close()
