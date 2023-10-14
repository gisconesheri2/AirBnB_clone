#!/usr/bin/python3
"""test suite for BaseModel class"""
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """tests for the BaseModel classes"""

    def test_uuid(self):
        """test the generation if the id"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertTrue(type(base1.id) == str)
        self.assertFalse(base1.id == base2.id)

    def test_datetime(self):
        """test datetime objects update and are converted properly"""
        base3 = BaseModel()
        base3.save()
        self.assertTrue(base3.updated_at > base3.created_at)
        int_dict = base3.to_dict()
        self.assertTrue(type(int_dict['created_at']) == str)

    def test_object_instantiation_from_dict(self):
        """test a new object is created using attributes passed via a dict"""
        base4 = BaseModel()
        base4.name = "My first model"
        base4.number = 89
        base_dict = base4.to_dict()
        base5 = BaseModel(**base_dict)
        dt = datetime.now()

        self.assertTrue(base4.id == base5.id)
        self.assertTrue(base4.name == base5.name)
        self.assertTrue(base4.number == base5.number)
        self.assertFalse(base4 is base5)
