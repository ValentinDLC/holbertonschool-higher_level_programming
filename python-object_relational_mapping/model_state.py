#!/usr/bin/python3
"""State model for SQLAlchemy.

This module defines:
- Base: declarative_base()
- State: mapped to table 'states'
Comments are in English, studious tone.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State class mapped to the 'states' table.

    - id: auto-increment integer primary key, not nullable
    - name: string up to 128 characters, not nullable
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
