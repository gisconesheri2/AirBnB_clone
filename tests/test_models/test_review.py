#!/usr/bin/python3
"""test suite for Review class"""
from datetime import datetime
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """tests for the Review classes"""

    def test_uuid(self):
        """test the generation if the id"""
        review1 = Review()
        review2 = Review()
        self.assertTrue(type(review1.id) == str)
        self.assertFalse(review1.id == review2.id)

    def test_datetime(self):
        """test datetime objects update and are converted properly"""
        review3 = Review()
        review3.save()
        self.assertTrue(review3.updated_at > review3.created_at)
        int_dict = review3.to_dict()
        self.assertTrue(type(int_dict['created_at']) == str)

    def test_object_instantiation_from_dict(self):
        """test a new object is created using attributes passed via a dict"""
        review4 = Review()
        review4.place_id = "My first model"
        review4.user_id = "rest"
        review4.text = "root"
        review_dict = review4.to_dict()
        review5 = Review(**review_dict)
        dt = datetime.now()

        self.assertTrue(review4.id == review5.id)
        self.assertTrue(review4.place_id == review5.place_id)
        self.assertTrue(review4.user_id == review5.user_id)
        self.assertTrue(review4.text == review5.text)
        self.assertTrue(type(review4.created_at) == type(dt))
        self.assertFalse(review4 is review5)
