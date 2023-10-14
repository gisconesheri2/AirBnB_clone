#!/usr/bin/python3
"""model for a user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """model for a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, **kwargs):
        """initializes the class and the parent class"""
        super().__init__(**kwargs)
