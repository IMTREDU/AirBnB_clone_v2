#!/usr/bin/python3
"""Defines the Amenity class"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Represents an Amenity
    Attributes:
        name: name of the amenity
    """

    __tablename__ = 'amenities'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place',
                                       secondary=place_amenity,
                                       back_populates='amenities')
    else:
        name = ""
