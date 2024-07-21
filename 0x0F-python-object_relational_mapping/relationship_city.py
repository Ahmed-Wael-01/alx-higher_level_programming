#!/usr/bin/python3

"""
create state model with sqlalchemy
"""
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    states class that mappes to states table
    """
    __tablename__ = 'cities'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer(), ForeignKey('states.id'))
