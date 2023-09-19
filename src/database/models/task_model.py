""" Model class of the task table of the database"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.config.database_configuration import Base


class Task(Base):
    """
    Class for article table of the database where the article table
    is defined, created, and updated for SQL Alchemy.

    Args:
        Base (_type_): The instance of the declarative base of the
        configuration of conection to database.
    """

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), unique=True, index=True)
    content = Column(String(500))
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    category_id = Column(Integer, ForeignKey("categories.id"))

    # The name of variable is a string of the back_populates
    category = relationship("Category", back_populates="tasks")
