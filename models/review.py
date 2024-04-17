#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Represents a review in a MySQL database.

    Inherits from SQLAlchemy Base and corresponds to the MySQL table reviews.

    Attributes:
        __tablename__ (str): The name of the MySQL table for storing reviews.
        text (sqlalchemy String): The description of the review.
        place_id (sqlalchemy String): The ID of the place being reviewed.
        user_id (sqlalchemy String): The ID of the user who made the review.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
