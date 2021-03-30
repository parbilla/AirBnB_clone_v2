#!/usr/bin/python3
"""State Class"""
import os
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """Defines State Class"""
    if storage_type == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="delete")
    else:
        name = ''

        @property
        def cities(self):
            """Getter attribute that returns the list of City instances
            of the current State"""
            city_list = []
            for city in models.storage.all('City').values():
                if city.state.id == self.id:
                    city_list.append(city)
            return city_list
