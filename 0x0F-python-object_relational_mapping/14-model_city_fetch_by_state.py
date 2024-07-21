#!/usr/bin/python3
"""
lists all the state objects from the db
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State, City).filter(City.state_id == State.id).all()
    for state in states:
        print('{}: ({}) {}'.format(state[0].name, state[1].id, state[1].name))
