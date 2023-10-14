#!/usr/bin/python3
"""model for a useri review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """model for a user review
    Class Attributes:
        place_id (str) - Place.id
        user_id (Str) - User.id
        test (str)
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, **kwargs):
        """initializes the class and the parent class"""
        super().__init__(**kwargs)
