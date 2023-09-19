""" File for creating a schema of categories of the database """
from pydantic import BaseModel, validator
from src.utils.validators.string_validator import string_space_validator


class ICategoryData(BaseModel):
    """
    Class for creating a category schema of categories of the database
    when do have the following attributes:

    Attributes:
        name: The name of the category
        description: The description of the category
        is_deleted: True if the category is deleted and False otherwise

    Args:
        BaseModel (_type_): The base model instance of Pydantic
    """

    name: str
    description: str

    # pylint: disable=no-self-argument
    @validator("name")
    def name_must_contain_content(cls, value) -> str:
        """The values isn't only spaces in the name."""
        return string_space_validator(value, "Name must contain content")

    @validator("description")
    def description_must_contain_content(cls, value) -> str:
        """The values isn't only spaces in the description."""
        return string_space_validator(value, "Description must contain content")

    class Config:
        """Class for active configuration of the ORM of SQLAlchemy"""

        from_attributes = True
