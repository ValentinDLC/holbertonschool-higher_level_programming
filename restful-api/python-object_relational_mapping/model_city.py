#!/usr/bin/python3
"""City model for SQLAlchemy.

City inherits Base from model_state to ensure the same metadata and
proper foreign key relation to states.id.
Studious English comments.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base  # import Base from model_state as requested


class City(Base):
    """City class mapped to the 'cities' table.

    - id: auto-increment integer primary key, not nullable
    - name: string up to 128 chars, not nullable
    - state_id: integer foreign key referencing states.id, not nullable
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
