#!/usr/bin/python3
"""model for a city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """model for a city"""

    name = ""
    state_id = ""

    def __init__(self, **kwargs):
        """initializes the class and the parent class"""
        super().__init__(**kwargs)
