#!/usr/bin/python3
"""script that deletes all State objects with a name containing the letter a"""

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

    del_states = session.query(State).filter(State.name.contains('a')).all()

    for del_state in del_states:
        session.delete(del_state)

    session.commit()
