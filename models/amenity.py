#!/usr/bin/python3
"""model for a amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """model for amenity"""

    name = ""

    def __init__(self, **kwargs):
        """initializes the class and the parent class"""
        super().__init__(**kwargs)
