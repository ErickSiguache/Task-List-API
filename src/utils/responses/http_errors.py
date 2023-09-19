""" Functions for creating error messages of response for the client """
from fastapi import HTTPException, status


def set_http_error_404(message: str) -> HTTPException:
    """
    Function for returning a 404 response exception.

    Args:
        message (str): Message to be returned when a 404 response
    """
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)
