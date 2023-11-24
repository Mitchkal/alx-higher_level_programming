#!/usr/bin/python3
"""
module 9-model_state_a
lists state objxets from db with a
"""


import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_a(username, password, database):
    """
    module fetch first
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco")

    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)

    session.commit()
    session.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    create_a(username, password, database)
