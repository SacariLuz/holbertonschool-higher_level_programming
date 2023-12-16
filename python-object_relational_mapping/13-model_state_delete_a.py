#!/usr/bin/python3

"""
Script que elimina todos los obejtos de estado.
Un nombre que contenga la letra a' de la database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
            State.name.contains('a')).delete(
                    synchronize_session=False)

    session.flush()
    session.commit()
    session.close()
