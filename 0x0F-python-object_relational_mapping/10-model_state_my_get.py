#!/usr/bin/python3
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
"""
module 10-model_search state
finds and returns id of searched state
"""


def state_fetch_first(username, password, database, state_name):
    """
    module fetch first
    returns id of searched state
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1], \
     sys.argv[2], sys.argv[3], sys.argv[4]
    state_fetch_first(username, password, database, state_name)
