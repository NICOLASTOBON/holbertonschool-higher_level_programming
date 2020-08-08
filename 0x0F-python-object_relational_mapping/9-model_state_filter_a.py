#!/usr/bin/python3
"""script that lists all State objects that contain the letter a
from the database"""

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
        .format(username, password, name_db), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    contains = session.query(State)\
        .filter(State.name.contains('a'))\
        .order_by(State.id)\
        .all()

    for contain in contains:
        print('{}: {}'.format(contain.id, contain.name))
