#!/usr/bin/env python3
"""
User Module
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """
    User class
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
<<<<<<< HEAD
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
=======
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self):
        """
        String Rep
        """
        return f"User: id={self.id}"
>>>>>>> b4026bd5ab24c1d27603143f87446571fd8584f8
