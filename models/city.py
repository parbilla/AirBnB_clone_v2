#!/usr/bin/python3
"""City Class"""
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """Defines City Class"""
    if storage_type == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey(states.id), nullable=False,)
        places = relationship('Place', backref='cities', cascade='delete')
    else:
        state_id = ''
        name = ''
