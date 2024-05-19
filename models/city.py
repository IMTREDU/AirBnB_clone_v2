#!/usr/bin/python3
"""Defines the City class"""

import os
from models.base_model import BaseModel, Base, Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Represents a City
    Attributes:
        state_id: the state id
        name: name of the city
    """

    __tablename__ = 'cities'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state = relationship(
            'State', back_populates='cities')
    else:
        name = ""
        state_id = ""
