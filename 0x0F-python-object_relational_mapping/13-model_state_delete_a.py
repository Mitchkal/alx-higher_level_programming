#!/usr/bin/python3
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
"""
module 13-model_state_delete_a
deletes state objects from dtatabase with a
"""


def delete_state(username, password, database):
    """
    module fetch first
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        session.delete(state)

    session.commit()

    session.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    delete_state(username, password, database)
