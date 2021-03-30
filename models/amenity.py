#!/usr/bin/python3
"""Amenity Class"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from models.place import place_amenity
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    """Defines Amenity Class"""
    if storage_type == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       backref="amenities", cascade="delete")
    else:
        name = ''
