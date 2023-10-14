#!/usr/bin/python3
"""serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
import os.path
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """handle the serialization and deserialization of JSON
    to python objects
    """

    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj with the key (obj class name.id)
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to __file_path"""
        inst_dict = {}
        for k, v in FileStorage.__objects.items():
            inst_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf8') as fp:
            json.dump(inst_dict, fp)

    def reload(self):
        """deserialize from JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding='utf8') as fp:
                try:
                    inst_dict = json.load(fp)
                    for key, v in inst_dict.items():
                        class_name = key.split('.')[0]
                        try:
                            FileStorage.__objects[key] = eval(class_name)(**v)
                        except NameError as e:
                            print(f"{class_name} not valid as {e}")
                        except TypeError as e:
                            print(f"{e}")
                except json.decoder.JSONDecodeError:
                    os.unlink(os.path.abspath(FileStorage.__file_path))
