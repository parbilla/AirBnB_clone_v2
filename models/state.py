#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel), Base:
    """ State class """
    __tablename__ = "states"
    name =     name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

if os.getenv("HBNB_TYPE_STORAGE") == "fs":
        @property
        def cities(self):
            """ Returns list of City instance with equal state_id """
            my_list = []
            for city in storage.all("City").values():
                if city.state_id == self.id:
                    my_list.append(city)
            return my_list