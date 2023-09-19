""" File for creating a schema of categories of the database """
from typing import Optional
from src.modules.categories.schemas.category_data import ICategoryData


class ICategory(ICategoryData):
    """
    Class for creating a category schema of categories of the database
    when do have the following attributes:

    Attributes:
        id: The identifier of the category
        name: The name of the category
        description: The description of the category
        is_deleted: True if the category is deleted and False otherwise

    Args:
        CategoryData (_type_): Inherence of the category
    """

    id: int
    is_deleted: Optional[bool] = False
