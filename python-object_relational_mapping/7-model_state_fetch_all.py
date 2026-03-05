#!/usr/bin/python3
"""List all State objects from hbtn_0e_6_usa using SQLAlchemy.
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

    # Query all states ordered by id
    states = session.query(State).order_by(State.id).all()
    for st in states:
        print(f"{st.id}: {st.name}")

    session.close()
