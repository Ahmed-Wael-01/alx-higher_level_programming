#!/usr/bin/python3

"""
create state model with sqlalchemy
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    states class that mappes to states table
    """
    __tablename__ = 'cities'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer(), ForeignKey('states.id'))

    state = relationship("State", back_populates="cities")
