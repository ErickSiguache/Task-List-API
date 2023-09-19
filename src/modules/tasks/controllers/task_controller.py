""" Controller file for the control of queries in the routes """
from typing import Optional, List
from fastapi import APIRouter
from src.modules.categories.services.category_service import CategoryService
from src.modules.tasks.services.task_service import TaskService
from src.modules.tasks.schemas.task_id import ITask
from src.modules.tasks.schemas.task_data import ITaskData

task_route = APIRouter(prefix="/tasks", tags=["Task"])


# Instance of category class
category_service = CategoryService()
task_service = TaskService(category_service)


@task_route.get("/", response_model=Optional[List[ITask]])
def get_tasks() -> Optional[List[ITask]]:
    """jndj"""
    return task_service.get_tasks()


@task_route.post("/")
def create_task(new_task: ITaskData) -> Optional[ITask]:
    """dnd"""
    return task_service.insert_task(new_task)


@task_route.put("/")
def update_task(new_task: ITask) -> None:
    """njnddjd"""
    return task_service.update_task(new_task)
