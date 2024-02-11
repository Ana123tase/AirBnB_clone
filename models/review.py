#!/usr/bin/python3
"""Definition of class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representing a review.

    Attributes:
        place_id: Place idintifier
        user_id: Users identity
        text:  text review
    """

    place_id = ""
    user_id = ""
    text = ""
