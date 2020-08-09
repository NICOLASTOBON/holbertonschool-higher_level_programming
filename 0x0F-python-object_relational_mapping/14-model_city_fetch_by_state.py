#!/usr/bin/python3
""" script that prints all City objects """

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name_db = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, name_db)
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()

    for cy, st in rows:
        print('{}: ({}) {}'.format(st.name, cy.id, cy.name))
