#!/usr/bin/python3
"""State Module for HBNB project."""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Represents a state in a MySQL database.

    Inherits from SQLAlchemy Base and corresponds to the MySQL table states.

    Attributes:
        __tablename__ (str): The name of the MySQL table for storing states.
        name (sqlalchemy String): The name of the state.
        cities (sqlalchemy relationship): The relationship between state and cities.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Returns a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
