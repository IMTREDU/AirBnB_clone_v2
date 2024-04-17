#!/usr/bin/python3
"""Module defines a base class for all models in our hbnb clone"""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String

Base = declarative_base()


class BaseModel(Base):
    """Defines the BaseModel class.

    Attributes:
        id (sqlalchemy String): The unique identifier for the BaseModel.
        created_at (sqlalchemy DateTime): The timestamp of creation.
        updated_at (sqlalchemy DateTime): The timestamp of the last update.
    """

    __tablename__ = 'base_model'

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key-value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """Updates the updated_at attribute with the current datetime
        and saves the instance to the storage.
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance,
        including the class name (__class__) and timestamps in ISO format.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.pop("_sa_instance_state", None)
        return my_dict

    def delete(self):
        """Deletes the current instance from storage."""
        models.storage.delete(self)

    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)
