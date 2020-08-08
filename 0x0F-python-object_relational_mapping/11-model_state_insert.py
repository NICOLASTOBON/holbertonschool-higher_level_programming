#!/usr/bin/python3
# script that adds the State object “Louisiana” to the database

from model_state import Base, State
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
    session.add(State(name='Louisiana'))

    states = session.query(State).filter(State.name == 'Louisiana').first()
    print(states.id)

    session.commit()
