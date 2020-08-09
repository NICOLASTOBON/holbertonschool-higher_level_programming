#!/usr/bin/python3
""" python file """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base
from sqlalchemy.orm import relationship


class State(Base):
    """ class city """
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement='auto',
        nullable=False,
        unique=True
    )

    name = Column(
        String(128),
        nullable=False
    )

    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete"
    )
