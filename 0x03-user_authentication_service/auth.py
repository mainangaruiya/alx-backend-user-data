#!/usr/bin/env python3
"""auth related routines
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User

def _hash_password(password: str) -> bytes:
    """Password hashing
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Adds a new user to the database
        """
        try:
            # Check if the user already exists
            self._db.find_user_by(email=email)
        except NoResultFound:
            # If the user doesn't exist, add the new user
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)
        # If the user already exists, raise a ValueError
        raise ValueError("User {} already exists".format(email))
