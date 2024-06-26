#!/usr/bin/python3
"""This module defines the file storage class for AirBnB"""
import json
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Handles serialization of instances to a JSON file and
    deserialization of JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: stores all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary
        Return:
            a dictionary of __objects
        """
        if cls is None:
            return self.__objects
        else:
            new_dict = {}
            if len(self.__objects) > 0:
                for key, value in self.__objects.items():
                    if type(cls) is str:
                        if cls == key.split('.')[0]:
                            new_dict[key] = value
                    else:
                        if cls is type(value):
                            new_dict[key] = value
            return new_dict

    def new(self, obj):
        """Sets __objects to given obj
        Args:
            obj: the object to set
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if present
        Not sure if it should also delete from JSON file
        """
        dict_key = ""
        for key, value in self.__objects.items():
            if obj == value:
                dict_key = key
        if dict_key:
            del self.__objects[dict_key]

    def close(self):
        """Calls reload() to deserialize the JSON file to objects"""
        self.reload()
