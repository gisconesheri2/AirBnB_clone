#!/usr/bin/python3
"""test suite for Amenity class"""
from datetime import datetime
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """tests for the Amenity classes"""

    def test_uuid(self):
        """test the generation if the id"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertTrue(type(amenity1.id) is str)
        self.assertFalse(amenity1.id == amenity2.id)

    def test_datetime(self):
        """test datetime objects update and are converted properly"""
        amenity3 = Amenity()
        amenity3.save()
        self.assertTrue(amenity3.updated_at > amenity3.created_at)
        int_dict = amenity3.to_dict()
        self.assertTrue(type(int_dict['created_at']) is str)

    def test_object_instantiation_from_dict(self):
        """test a new object is created using attributes passed via a dict"""
        amenity4 = Amenity()
        amenity4.name = "resr@peace"
        amenity_dict = amenity4.to_dict()
        amenity5 = Amenity(**amenity_dict)
        dt = datetime.now()

        self.assertTrue(amenity4.id == amenity5.id)
        self.assertTrue(amenity4.name == amenity5.name)
        self.assertTrue(type(amenity4.created_at) is type(dt))
        self.assertFalse(amenity4 is amenity5)
