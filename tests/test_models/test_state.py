#!/usr/bin/python3
"""test suite for State class"""
from datetime import datetime
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """tests for the State classes"""

    def test_uuid(self):
        """test the generation if the id"""
        state1 = State()
        state2 = State()
        self.assertTrue(type(state1.id) == str)
        self.assertFalse(state1.id == state2.id)

    def test_datetime(self):
        """test datetime objects update and are converted properly"""
        state3 = State()
        state3.save()
        self.assertTrue(state3.updated_at > state3.created_at)
        int_dict = state3.to_dict()
        self.assertTrue(type(int_dict['created_at']) == str)

    def test_object_instantiation_from_dict(self):
        """test a new object is created using attributes passed via a dict"""
        state4 = State()
        state4.name = "resr@peace"
        state_dict = state4.to_dict()
        state5 = State(**state_dict)
        dt = datetime.now()

        self.assertTrue(state4.id == state5.id)
        self.assertTrue(state4.name == state5.name)
        self.assertTrue(type(state4.created_at) == type(dt))
        self.assertFalse(state4 is state5)
