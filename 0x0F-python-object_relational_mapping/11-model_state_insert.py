#!/usr/bin/python3

"""
module 11-model_state_insert
insert and retruns id of state
"""


import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def state_insert(username, password, database):
    """
    method state_insert
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    lousiana = State(name="Louisiana")
    session.add(lousiana)
    session.commit()

    print(lousiana.id)

    session.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    state_insert(username, password, database)
