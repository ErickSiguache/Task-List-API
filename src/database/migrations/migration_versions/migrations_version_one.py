"""The module for creating the category table in the database of version one"""
from src.config.database_configuration import engine, Base
from src.database.models.category_model import Category
from src.database.models.task_model import Task


def create_tables_version_one() -> None:
    """
    Function for initializing the database and creating all tables
    """
    _ = (Category, Task)

    Base.metadata.create_all(bind=engine)
