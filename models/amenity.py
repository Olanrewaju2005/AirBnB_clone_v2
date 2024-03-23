#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from models.place import place_amenity

class Amenity(BaseModel, Base):
    """ This is the class for amenity """
    __tablename__ = "amenties"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
