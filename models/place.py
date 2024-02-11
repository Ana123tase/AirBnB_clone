#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id: City's ID
        user_id: User's ID
        name: place's name(s)
        description: Brief overview opf the city
        max_guest: Max_num of guests place can hold at a time
        price_by_night: Total price per night          
        number_bathrooms: The present numer of bathrooms in a pave
        latitude (float): latitude
        longitude: longitudes
        amenity_ids: New identities
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
