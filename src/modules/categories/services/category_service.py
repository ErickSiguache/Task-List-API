""" File for a create the CRUD operations for the category table """
from typing import Optional, List
from sqlalchemy import and_
from src.database.models.category_model import Category
from src.utils.open_close_database_operation import use_db_session
from src.modules.categories.schemas.category_data import ICategoryData
from src.modules.categories.schemas.category_id import ICategory
from src.utils.models_enums_values import ModelValues
from src.utils.responses.http_errors import set_http_error_404
from src.utils.responses.json_errors import response_error_404


class CategoryService:
    """
    Class for constructing of the CRUD methods for category models. The
    class is responsible of sending and receiving the information about
    category models and inserting in the database and returning the
    results.
    """

    def __init__(self):
        self.session = None

    @use_db_session
    def get_categories(self) -> Optional[List[ICategory]]:
        """
        Get the list of categories of the category models and return
        the list of categories.

        Returns:
            Optional[List[ICategory]]: The list of categories of the
            database.
        """
        categories = (
            self.session.query(Category)
            .filter(Category.is_deleted == ModelValues.IS_DELETED_FALSE.value)
            .all()
        )
        if not categories:
            set_http_error_404("Error: The database is empty")
        return categories

    @use_db_session
    def __get_category_by_name(self, category_name) -> Optional[ICategory]:
        """Returns a category if it exists"""
        return (
            self.session.query(Category).filter(Category.name == category_name).first()
        )

    @use_db_session
    def get_categories_by_name(self, category_name: str) -> ICategory:
        """
        Get a category by name of the category models and return
        the list of categories.
        """
        category = self.__get_category_by_name(category_name)
        if not category:
            set_http_error_404("Error: The category not found")
        return category

    @use_db_session
    def get_category_by_id(self, category_id: int) -> Optional[ICategory]:
        """Returns a category if it exists"""
        print("Si entro")
        return self.session.query(Category).filter(Category.id == category_id).first()

    @use_db_session
    def get_categories_by_id(self, category_id: int) -> ICategory:
        """
        Get a category by name of the category models and return
        the list of categories.
        """
        category = self.get_category_by_id(category_id)
        if not category:
            set_http_error_404("Error: The category not exist")
        return category

    @use_db_session
    def add_category(self, category: ICategoryData) -> ICategory:
        """
        Get the data for the category and create a new category for
        insert in the database and return the new category of the
        database.

        Args:
            new_category (ICategoryData): The category data to insert
            with the information:
                name: string, the name of the category.
                description: string, the description of the category
                is_deleted: boolean, when false for default and can't
                be modified.

        Returns:
            ICategory: The new category inserted in the database.

        Exceptions:
            Error 404: The category name already exists.
        """
        if self.__get_category_by_name(category.name):
            return response_error_404("The category name already exists")

        category = Category(name=category.name, description=category.description)
        self.session.add(category)
        self.session.commit()
        self.session.refresh(category)
        return category

    @use_db_session
    def __get_category_by_id_name(self, id_cat: int, category_name: str) -> ICategory:
        """Returns a category if it exists"""
        return (
            self.session.query(Category)
            .filter(and_(Category.name == category_name, Category.id != id_cat))
            .first()
        )

    @use_db_session
    def update_category(self, category: ICategory):
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
        if not self.get_category_by_id(category.id):
            return response_error_404("The category not exist")

        if self.__get_category_by_id_name(category.id, category.name):
            return response_error_404("The category name already exists")

        self.session.query(Category).filter(Category.id == category.id).update(
            {
                Category.name: category.name,
                Category.description: category.description,
            }
        )
        self.session.commit()

    @use_db_session
    def update_state_category(self, id_cat: int, status: int):
        """
        The function for updating the status of category in the
        database.

        Args:
            id (int): The identifier of the category
            status (int): The status of the category
        """
        if not self.get_category_by_id(id_cat):
            return response_error_404("The category not exist")

        status_category = (
            False if status == ModelValues.IS_DELETED_FALSE.value else True
        )
        self.session.query(Category).filter(Category.id == id_cat).update(
            {Category.is_deleted: status_category}
        )
        self.session.commit()
