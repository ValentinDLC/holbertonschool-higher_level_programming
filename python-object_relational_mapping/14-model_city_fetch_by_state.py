#!/usr/bin/python3
"""Print all City objects from the database hbtn_0e_14_usa.
Format: <state name>: (<city id>) <city name>
Studious English comments.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Join City and State, order by City.id as requested
    results = session.query(City, State).join(State, City.state_id == State.id).order_by(City.id).all()
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
