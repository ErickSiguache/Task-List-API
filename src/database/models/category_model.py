""" Model class of the category table of the database"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from src.config.database_configuration import Base


class Category(Base):
    """
    Class for category table of the database where the category table
    is defined, created, and updated for SQL Alchemy.

    Args:
        Base (_type_): The instance of the declarative base of the
        configuration of conection to database.
    """

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(String(200))
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # back_populates is to get all the tasks of a category.
    tasks = relationship("Task", back_populates="category")
