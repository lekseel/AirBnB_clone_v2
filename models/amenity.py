#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Amenity(BaseModel, Base):
        """ State Class """

        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)

else:
    class Amenity(BaseModel):
        """ State Class """
        name = ""
