#!/usr/bin/env python3
"""
model
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class User(Base):
	"""
	from user table
	"""
	__tablename__="users"
	id = column(Integer, primary_key=True)
	email = column(String(250), nullable=False)
	hashed_password = Column(String(250),nullable=False)
	session_id = Column(String(250), nullable=True)
	reset_token = Column(String(250), nullable=True)