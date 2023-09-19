""" Function for returning a JSON Response if there is a mistake """
from fastapi import status
from fastapi.responses import JSONResponse


def response_error_404(message_error: str) -> JSONResponse:
    """
    Response a error of the type 404 with a message of the error and
    return a JSON Response.

    Args:
        message_error (str): Message of the error

    Returns:
        JSONResponse: The JSON Response of the error with the error
        message and the status code 404
    """
    return JSONResponse(
        content={
            "status": status.HTTP_404_NOT_FOUND,
            "message": message_error,
        },
        status_code=status.HTTP_404_NOT_FOUND,
    )
