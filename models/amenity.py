#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represents an amenity in a MySQL database.

    Inherits from SQLAlchemy Base and corresponds to the MySQL table amenities.

    Attributes:
        __tablename__ (str): The name of the MySQL table for storing amenities.
        name (sqlalchemy String): The name of the amenity.
        place_amenities (sqlalchemy relationship): The relationship between place and amenities.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity", viewonly=False)
