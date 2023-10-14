#!/usr/bin/python3
"""test suite for Place class"""
from datetime import datetime
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """tests for the Place classes"""

    def test_uuid(self):
        """test the generation if the id"""
        place1 = Place()
        place2 = Place()
        self.assertTrue(type(place1.id) is str)
        self.assertFalse(place1.id == place2.id)

    def test_datetime(self):
        """test datetime objects update and are converted properly"""
        place3 = Place()
        place3.save()
        self.assertTrue(place3.updated_at > place3.created_at)
        int_dict = place3.to_dict()
        self.assertTrue(type(int_dict['created_at']) is str)

    def test_object_instantiation_from_dict(self):
        """test a new object is created using attributes passed via a dict"""
        place4 = Place()
        place4.name = "My first model"
        place4.city_id = "3233v323"
        place4.user_id = "576762bu29h"
        place4.description = "in a safe place"
        place4.number_rooms = 4
        place4.number_bathrooms = 2
        place4.max_guest = 10
        place4.price_by_night = 100
        place4.latitude = 1333.222
        place4.longitude = 3444.534
        place_dict = place4.to_dict()
        place5 = Place(**place_dict)
        dt = datetime.now()

        self.assertTrue(place4.id == place5.id)
        self.assertTrue(place4.name == place5.name)
        self.assertTrue(place4.city_id == place5.city_id)
        self.assertTrue(place4.user_id == place5.user_id)
        self.assertTrue(place4.number_rooms == place5.number_rooms)
        self.assertTrue(place4.number_bathrooms == place5.number_bathrooms)
        self.assertTrue(place4.max_guest == place5.max_guest)
        self.assertTrue(place4.price_by_night == place5.price_by_night)
        self.assertTrue(place4.latitude == place5.latitude)
        self.assertTrue(place4.longitude == place5.longitude)
        self.assertTrue(type(place4.created_at) is type(dt))
        self.assertFalse(place4 is place5)
