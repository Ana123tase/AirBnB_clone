#!/usr/bin/python3
"""Definition the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Representation of a state.

    Attributes:
        name (str): State's name
    """

    name = ""

