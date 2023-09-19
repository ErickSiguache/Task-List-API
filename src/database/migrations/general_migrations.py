"""The module for creating all tables in the database"""
from src.database.migrations.migration_versions.migrations_version_one import (
    create_tables_version_one,
)


# Create the tables in the database
def initialize_database() -> None:
    """
    Function for initializing the database and creating all tables
    """
    create_tables_version_one()
