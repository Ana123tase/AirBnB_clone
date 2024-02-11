#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity/a newcomer!

    Attributes:
        name: name of the amenity (str).
    """

    name = ""
