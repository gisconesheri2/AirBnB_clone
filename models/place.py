#!/usr/bin/python3
"""model for a place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """model for a Place
    class Attributes:
        city_id (str) - City.id
        user_id (str) - User.id
        name (str) - name for place
        description (str)
        number_rooms (int)
        max_guest (int)
        price_by_night (int)
        latitude (float)
        longitude (float)
        amenity_ids (list of string) - list of Amenity.id
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

    def __init__(self, **kwargs):
        """initialize the class as well as parent class"""
        super().__init__(**kwargs)
