""" Function for validating data of the string type """


def string_space_validator(value: str, message_error: str) -> str:
    """
    Function for validating data of the string type when data have
    spaces.

    Args:
        value (str): Value to be validated.
        message_error (str): Message error for the value.

    Raises:
        ValueError: Message error when the value have spaces.

    Returns:
        str: Value to be validated if the value has not spaces.
    """
    if not value.strip():
        raise ValueError(message_error)
    return value
