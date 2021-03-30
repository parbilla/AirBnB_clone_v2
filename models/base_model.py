#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from models import storage
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)    

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        """if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.__set_attributes(kwargs)
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)"""
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()

    def __set_attributes(self, attr_dict):
        """ __set_attributes method """

        if 'id' not in attr_dict:
            attr_dict['id'] = str(uuid4())

        if 'created_at' not in attr_dict:
            attr_dict['created_at'] = datetime.now()

        elif not isinstance(attr_dict['created_at'], datetime):
            attr_dict['created_at'] = datetime.strptime(
                attr_dict['created_at'], '%Y-%m-%d %H:%M:%S.%f')

        if 'updated_at' in attr_dict:
            if not isinstance(attr_dict['updated_at'], datetime):
                attr_dict['updated_at'] = datetime.strptime(
                    attr_dict['updated_at'], '%Y-%m-%d %H:%M:%S.%f')

        if attr_dict['__class__']:
            attr_dict.pop('__class__')
        for key, val in attr_dict.items():
            setattr(self, key, val)


    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        for key, value in (self__dict__).items():
            if (key == '_sa_instance_state'):
                del key
        return dictionary

    def delete(self):
        """Delete current instance from storage"""
        models.storage.delete(self)
