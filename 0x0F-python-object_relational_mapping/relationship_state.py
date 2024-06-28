#!/usr/bin/python3

"""
create state model with sqlalchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    states class that mappes to states table
    """
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128))
    cities = relationship("City", backref="state", cascade="all, delete")
