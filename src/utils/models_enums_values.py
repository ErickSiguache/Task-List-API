""" Schema for the enums values of the models of the database """
from enum import Enum


class ModelValues(Enum):
    """
    The class represents the enum values for the data of all models and
    states of this information.

    Args:
        Enum (str | int): The values of the enum for the models and
        states of the models in the database.
    """

    IS_DELETED_FALSE = 0
    IS_DELETED_TRUE = 1
    TRUE_VALUES = "true"
    FALSE_VALUES = "false"
