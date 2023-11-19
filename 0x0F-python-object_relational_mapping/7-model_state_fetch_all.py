#!/usr/bin/python3
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import Session
"""
module7-model_state_fetch_all
lists all state objects from dtatabase
"""


def state_fetch_all(username, password, database):
    """
    module fetchall
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    session = Session(engine)

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    state_fetch_all(username, password, database)
