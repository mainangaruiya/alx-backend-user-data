#!/usr/bin/env python3
"""module for pswd enc
"""
import bcrypt

def hash_password(password: str) -> bytes:
	"""random encr with gensalt
	"""
	return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def is_valid(hashed_password: bytes, password: str) -> bool:
	"""check if hash is from the password given 
	"""
	return bcrypt.checkpw(password.encode('utf-8'), hashed_password)