#!/usr/bin/python3
"""Defines the State class"""
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Represents a State
    Attributes:
        name: name of the state
        cities: relationship between state and city tables
    """

    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City', back_populates='state',
            cascade='all, delete, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """Returns a list of City instances related to this State"""
            cities_instances = []
            cities_dict = models.storage.all(models.City)
            for key, value in cities_dict.items():
                if self.id == value.state_id:
                    cities_instances.append(value)
            return cities_instances
