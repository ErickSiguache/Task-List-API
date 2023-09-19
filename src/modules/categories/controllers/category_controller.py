""" Controller file for the control of queries in the routes """
from typing import Optional, List
from fastapi import APIRouter
from src.modules.categories.services.category_service import CategoryService
from src.modules.categories.schemas.category_id import ICategory
from src.modules.categories.schemas.category_data import ICategoryData


category_route = APIRouter(prefix="/categories", tags=["category"])


# Instance of category class
category_service = CategoryService()


@category_route.get("/", response_model=Optional[List[ICategory]], status_code=200)
def get_categories() -> Optional[List[ICategory]]:
    """
    Returns a list of categories of the database or a status code if no
    category in the database.

    Information:

        Returns:
            List of categories => The list of categories or the
            exception if no category in the database.

        Exception:
            Error 404 => The database is empty.
    """
    categories = category_service.get_categories()
    return categories


@category_route.get("/name={name}", response_model=Optional[ICategory], status_code=200)
def get_category_by_name(name: str) -> Optional[ICategory]:
    """
    The function returns a category of the database and returns a error
    if it is not found.

    Args:
        name (str): The name of the category in the database.

    Returns:
        Optional[ICategory]: A category of the database or error if it
        is not found.s
    """
    category = category_service.get_categories_by_name(name)
    return category


@category_route.get("/id={id_cat}", response_model=Optional[ICategory], status_code=200)
def get_category(id_cat: int) -> Optional[ICategory]:
    """
    The function returns a category of the database and returns a error
    if it is not found.

    Args:
        id_cat (int): The Identifier of the category in the database.

    Returns:
        Optional[ICategory]: A category of the database or error if it
        is not found.
    """
    category = category_service.get_categories_by_id(id_cat)
    return category


@category_route.post("/", status_code=201)
def post_category(category: ICategoryData) -> None:
    """
    Get the data for the category and return the category inserted or
    exception if the category wasn't inserted.

    Information:

        Args:
            Category Data => The category data to insert:
            name (string): The name of the category.
            description (string): The description of the category

        Returns:
            Category => The new category inserted in the database.

        Exceptions:
            Error 404 => The category name already exists.
            Error 422 => Validation error of the category data.
    """
    return category_service.add_category(category)


@category_route.put("/", status_code=201)
def put_category(category: ICategory) -> Optional[ICategory]:
    """
    The function for updating the category in the database.

    Args:
        category (ICategory) => The category to update with the
        information:
            name (string): The name of the category.
            description (string): The description of the category


    Returns:
        Optional[ICategory]: The category to update if the
        category was successfully or an exception if the category
        was not updated.
    """
    return category_service.update_category(category)


@category_route.patch("/id={id_cat}/status={status}", status_code=201)
def update_status_category(id_cat: int, status: int) -> Optional[ICategory]:
    """
    The function for updating the status of category in the
    database.

    Args:
        id (int): The identifier of the category
        status (int): The status of the category
    """
    return category_service.update_state_category(id_cat, status)
