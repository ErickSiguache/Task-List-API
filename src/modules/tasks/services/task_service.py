""" File for a create the CRUD operations for the task table """
from typing import Optional, List
from sqlalchemy import and_
from src.database.models.task_model import Task
from src.utils.open_close_database_operation import use_db_session
from src.modules.tasks.schemas.task_id import ITask
from src.modules.tasks.schemas.task_data import ITaskData
from src.utils.models_enums_values import ModelValues
from src.utils.responses.http_errors import set_http_error_404
from src.utils.responses.json_errors import response_error_404


class TaskService:
    """
    Class for constructing of the CRUD methods for tasks models. The
    class is responsible of sending and receiving the information about
    tasks models and inserting in the database and returning the
    results.
    """

    def __init__(self, categories_service):
        self.session = None
        self.categories_service = categories_service

    @use_db_session
    def get_tasks(self) -> Optional[List[ITask]]:
        """
        Get the list of tasks of the Task models and return
        the list of tasks.

        Returns:
            Optional[List[ITask]]: The list of tasks of the
            database.
        """
        tasks = (
            self.session.query(Task)
            .filter(Task.is_deleted == ModelValues.IS_DELETED_FALSE.value)
            .all()
        )
        if not tasks:
            set_http_error_404("Error: The database is empty")
        return tasks

    @use_db_session
    def __get_task_by_name(self, task_title: str) -> Optional[ITask]:
        """Returns a task if it exists"""
        return self.session.query(Task).filter(Task.title == task_title).first()

    @use_db_session
    def __get_task_by_id(self, task_id: str) -> Optional[ITask]:
        """Returns a task if it exists"""
        return self.session.query(Task).filter(Task.id == task_id).first()

    @use_db_session
    def insert_task(self, new_task: ITaskData) -> Optional[ITask]:
        """
        Get the data for the task and create a new task for
        insert in the database and return the new task of the
        database.

        Args:
            new_task (ITaskData): The task data to insert
            with the information:
                title: string, the title of the task.
                content: string, the content of the task
                is_deleted: boolean, when false for default and can't
                be modified.

        Returns:
            ITask: The new task inserted in the database.

        Exceptions:
            Error 404: The task name already exists.
        """
        if self.__get_task_by_name(new_task.title):
            return response_error_404("The task name already exists")

        if not self.categories_service.get_category_by_id(new_task.category_id):
            return response_error_404("The category not exist")

        task = Task(
            title=new_task.title,
            content=new_task.content,
            category_id=new_task.category_id,
        )
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    @use_db_session
    def __get_task_by_id_name(self, task_id: int, task_name: str) -> ITask:
        """Returns a task if it exists"""
        return (
            self.session.query(Task)
            .filter(and_(Task.title == task_name, Task.id != task_id))
            .first()
        )

    @use_db_session
    def update_task(self, task: ITask) -> None:
        """njfdn"""
        if not self.__get_task_by_id(task.id):
            return response_error_404("The task not exist")
        if self.__get_task_by_id_name(task.title, task.id):
            return response_error_404("The category name already exists")
        if not self.categories_service.get_category_by_id(task.category_id):
            return response_error_404("The category not exist")

        self.session.query(Task).filter(Task.id == task.id).update(
            {
                Task.title: task.title,
                Task.content: task.content,
                Task.category_id: task.category_id,
            }
        )
        self.session.commit()
