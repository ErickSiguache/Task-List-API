"""Data structure of the application 'Task List API'"""
from setuptools import setup, find_packages

setup(
    name="task-list-api",
    description="API for creating tasks in a database",
    author="Erick A. Siguache",
    version="0.1.0",
    packages=find_packages(where="src/"),
    package_dir={"": "src"},
)
