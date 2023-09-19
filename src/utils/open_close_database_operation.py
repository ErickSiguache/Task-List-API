""" Function for closing the connection and opening a new connection """
from functools import wraps
from typing import TypeVar, Generic, Callable, Any
from src.config.database_open_close_configuration import get_db


T = TypeVar("T", bound=Callable[..., Any])


def use_db_session(func: Generic[T]) -> Any:
    """
    Function that create a session and evaluate the function and close
    the connection to the database and return the result of the
    function.

    Args:
        func (Generic[T]): Function with an arbitrary number of
        arguments.

    Returns:
        Any: The return value of the function.
    """

    @wraps(func)
    def wrapped_func(self, *args, **kwargs):
        with get_db() as session:
            self.session = session
            return func(self, *args, **kwargs)

    return wrapped_func
