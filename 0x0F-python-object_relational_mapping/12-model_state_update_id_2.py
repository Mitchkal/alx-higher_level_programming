#!/usr/bin/python3
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
"""
module 12-model_state_updat
updates state objects in dtatabase
"""


def state_update(username, password, database):
    """
    module fetch first
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    state_update(username, password, database)
