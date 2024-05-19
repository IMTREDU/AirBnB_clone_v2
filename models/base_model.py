#!/usr/bin/python3
"""Defines the base model class for AirBnB"""
import uuid
import models
import os
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """Defines common attributes/methods for other classes"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialization of base model class
        Args:
            args: unused
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """Returns a string representation of the instance"""
        return self.__str__()

    def save(self):
        """Updates the public instance attribute updated_at to current time"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary representation of the instance
        Return:
            A dictionary of all key-value pairs in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in my_dict:
            del my_dict['_sa_instance_state']
        return my_dict

    def delete(self):
        """Deletes the current instance from storage"""
        models.storage.delete(self)
