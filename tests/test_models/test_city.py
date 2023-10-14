#!/usr/bin/python3
"""test suite for City class"""
from datetime import datetime
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """tests for the City classes"""

    def test_uuid(self):
        """test the generation if the id"""
        city1 = City()
        city2 = City()
        self.assertTrue(type(city1.id) is str)
        self.assertFalse(city1.id == city2.id)

    def test_datetime(self):
        """test datetime objects update and are converted properly"""
        city3 = City()
        city3.save()
        self.assertTrue(city3.updated_at > city3.created_at)
        int_dict = city3.to_dict()
        self.assertTrue(type(int_dict['created_at']) is str)

    def test_object_instantiation_from_dict(self):
        """test a new object is created using attributes passed via a dict"""
        city4 = City()
        city4.state_id = "My first model"
        city4.name = "rest"
        city_dict = city4.to_dict()
        city5 = City(**city_dict)
        dt = datetime.now()

        self.assertTrue(city4.id == city5.id)
        self.assertTrue(city4.state_id == city5.state_id)
        self.assertTrue(city4.name == city5.name)
        self.assertTrue(type(city4.created_at) is type(dt))
        self.assertFalse(city4 is city5)
