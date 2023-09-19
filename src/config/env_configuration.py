""" Configuration for using environment variables """
from os import getenv
from dotenv import load_dotenv


ROUTE_PATH_ENV = "src/environments/.env"
load_dotenv(ROUTE_PATH_ENV)


# Variables de entorno
DB_NAME = getenv("DB_NAME")
DB_HOST = getenv("DB_HOST")
DB_DIALECT = getenv("DB_DIALECT")
DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")
