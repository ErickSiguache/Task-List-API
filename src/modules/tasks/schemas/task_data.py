""" Model class of the task table of the database"""
from pydantic import BaseModel, validator
from src.utils.validators.string_validator import string_space_validator


class ITaskData(BaseModel):
    """
    Class for creating a task schema of tasks of the database
    when do have the following attributes:

    Attributes:
        title: The title of the task
        content: The content of the task
        category_id: The category id of the task

    Args:
        BaseModel (_type_): The base model instance of Pydantic
    """

    title: str
    content: str
    category_id: int

    # pylint: disable=no-self-argument
    @validator("title")
    def title_must_contain_content(cls, value) -> str:
        """The values isn't only spaces in the title."""
        return string_space_validator(value, "title must contain content")

    @validator("content")
    def maximum_content_length(cls, value) -> str:
        """The values don't exceed the maximum length"""
        characters = 499
        if len(value) >= characters:
            raise ValueError(
                f"The maximum length must be greater than {characters} characters"
            )
        return value

    class Config:
        """Class for active configuration of the ORM of SQLAlchemy"""

        from_attributes = True
