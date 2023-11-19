#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base

"""
module module_city
"""


Base = declarative_base()


class City(Base):
    """
    class definition of City
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
