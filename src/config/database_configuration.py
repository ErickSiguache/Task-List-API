"""Configuration for using the database"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config.env_configuration import (
    DB_HOST,
    DB_USER,
    DB_DIALECT,
    DB_NAME,
    DB_PASSWORD,
)


# URL configuration settings for connection to the database
URL_CONNECTIONS = f"{DB_DIALECT}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"


# Connection settings for connection to the database
engine = create_engine(URL_CONNECTIONS)
LocalSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()
