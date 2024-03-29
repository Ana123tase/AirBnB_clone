#!/usr/bin/python3
"""Defining class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """City representation

    Attributes:
        state_id: The state identifier
        name: The city's name
    """

    state_id = ""
    name = ""
