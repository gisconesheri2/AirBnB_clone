#!/usr/bin/python3
"""test the file_stoage.py"""
import unittest
import os
import os.path
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
import models


class TestFileStorage(unittest.TestCase):
    """test file storage"""

    def tearDown(self):
        """remove the file created"""
        if os.path.isfile("./file.json"):
            os.unlink(os.path.abspath("file.json"))

    def test_all(self):
        "test all functions in file_storage modeule"""
        keys_len = 0
        if os.path.isfile("./file.json"):
            keys_len = len(models.storage.all().keys())

        # creating new object calls the new() method
        user1 = User()

        # calling save on the object writes the object to the JSON file path
        user1.save()
        place1 = Place()
        place1.save()

        # calling .all() returns a dictionary of all objects saved on file
        # models.storage calls the reload() method in the background
        insts_dict = models.storage.all()
        self.assertTrue(len(insts_dict.keys()) == keys_len + 2)

        # an object created using another's attributes
        # should not call the new method be saved to file
        place_dict = place1.to_dict()
        place3 = Place(**place_dict)
        place3.save()
        self.assertTrue(len(insts_dict.keys()) == keys_len + 2)

    def test_file_path(self):
        """test file path type"""
        user1 = User()

        # calling save on the object writes the object to the JSON file path
        user1.save()
        place1 = Place()
        place1.save()
        self.assertTrue(os.path.isfile("./file.json"))
