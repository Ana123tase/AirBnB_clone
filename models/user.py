#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """User is the one who will fill in empty strings.

    Attributes:
        email (str): The email,emty
        password (str): The password, empty
        first_name (str): The first name is Empty
        last_name (str): Last name, Empty
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
