#!/usr/bin/env python3

"""
Module defining SQLAlchemy User model for the users table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy model for the users table.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    def __init__(self, email, hashed_password, session_id=None, reset_token=None):
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
        self.reset_token = reset_token

    def __repr__(self):
        return (
            f"<User(id={self.id}, email={self.email}, "
            f"session_id={self.session_id}, reset_token={self.reset_token})>"
        )

    def dummy_method(self):
        pass

    def another_dummy_method(self):
        pass
