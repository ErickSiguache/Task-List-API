""" File for creating a schema of tasks of the database """
from typing import Optional
from src.modules.tasks.schemas.task_data import ITaskData


class ITask(ITaskData):
    """
    Class for creating a task schema of tasks of the database
    when do have the following attributes:

    Attributes:
        id: The identifier of the task
        name: The name of the task
        content: The content of the task
        category_id: The category id of the task
        is_deleted: True if the task is deleted and False otherwise

    Args:
        TaskData (_type_): Inherence of the task
    """

    id: int
    is_deleted: Optional[bool] = False
