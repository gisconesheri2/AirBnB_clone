#!/usr/bin/python3
"""test suite for User class"""
from datetime import datetime
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """tests for the User classes"""

    def test_uuid(self):
        """test the generation if the id"""
        user1 = User()
        user2 = User()
        self.assertTrue(type(user1.id) == str)
        self.assertFalse(user1.id == user2.id)

    def test_datetime(self):
        """test datetime objects update and are converted properly"""
        user3 = User()
        user3.save()
        self.assertTrue(user3.updated_at > user3.created_at)
        int_dict = user3.to_dict()
        self.assertTrue(type(int_dict['created_at']) == str)

    def test_object_instantiation_from_dict(self):
        """test a new object is created using attributes passed via a dict"""
        user4 = User()
        user4.first_name = "My first model"
        user4.last_name = "rest"
        user4.password = "root"
        user4.email = "resr@peace"
        user_dict = user4.to_dict()
        user5 = User(**user_dict)
        dt = datetime.now()

        self.assertTrue(user4.id == user5.id)
        self.assertTrue(user4.first_name == user5.first_name)
        self.assertTrue(user4.last_name == user5.last_name)
        self.assertTrue(user4.password == user5.password)
        self.assertTrue(user4.email == user5.email)
        self.assertTrue(type(user4.created_at) == type(dt))
        self.assertFalse(user4 is user5)
