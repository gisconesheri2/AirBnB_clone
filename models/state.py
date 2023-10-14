#!/usr/bin/python3
"""model for a State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """model for a State"""

    name = ""

    def __init__(self, **kwargs):
        """initializes the class and the parent class"""
        super().__init__(**kwargs)
