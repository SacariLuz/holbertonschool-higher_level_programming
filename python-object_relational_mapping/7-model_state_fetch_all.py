#!/usr/bin/python3
"""
Script que enumera todos los objetos de estado de la database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        session.close()
