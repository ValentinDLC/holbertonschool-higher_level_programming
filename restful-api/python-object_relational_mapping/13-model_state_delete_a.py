#!/usr/bin/python3
"""Delete all State objects that contain the letter 'a' in their name.
Studious English comments.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states to delete (we choose to fetch and delete to be explicit)
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for st in states_to_delete:
        session.delete(st)
    session.commit()

    session.close()
