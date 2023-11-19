#!/usr/bin/python3
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
"""
module 8-model_state_fetch_all
lists first state objects from dtatabase
"""


def state_fetch_first(username, password, database):
    """
    module fetch first
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    state_fetch_first(username, password, database)
