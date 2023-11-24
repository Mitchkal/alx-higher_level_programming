#!/usr/bin/python3

"""
module 102-relationships
lists all city objects from db
"""


import sys
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker


def retrieve_city(username, password, database):
    """
    module 101-relationships
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City).order_by(City.id).all()

    for city in result:
        state_name = city.state.name if city.state else "No State"
        print("{}: {} -> {}".format(city.id, city.name, state_name))

    session.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    retrieve_city(username, password, database)
