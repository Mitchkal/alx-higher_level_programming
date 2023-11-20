#!/usr/bin/python3
"""
module 14-module_city_fetch_by_state
lists all cities in db
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_state(username, password, database_name):
    """
    fetches city by state
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
             username, password, database_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id):
        print('{}: {} {}'.format(city[0], city[1], city[2]))

    session.close()


if __name__ == "__main__":
    username, password, database_name = sys.argv[1], \
     sys.argv[2], sys.argv[3]

    fetch_state(username, password, database_name)
