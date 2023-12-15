#!/usr/bin/python3
"""
Define un State model
Hereda de SQLAlchemy Base y enlaces a los estados de tabla MySQL
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Representa estado para database
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
