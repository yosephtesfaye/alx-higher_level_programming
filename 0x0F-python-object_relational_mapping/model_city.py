#!/usr/bin/python3

""" City class model

"""

from model_state import Base

from sqlalchemy import Column, Integer, String, ForeignKey





class City(Base):

    """ City class inherits Base sqlalchemy call

    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)

    name = Column(String(128))
