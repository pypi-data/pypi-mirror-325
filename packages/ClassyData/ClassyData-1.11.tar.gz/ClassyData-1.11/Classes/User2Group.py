#!/usr/bin/env python3

'''
Created on 12/01/2015

@author: dedson
'''

import sqlalchemy
import sqlalchemy.orm

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.engine import reflection
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.collections import InstrumentedList, InstrumentedDict, InstrumentedSet

from .Base import Base

from .Accessor import Accessor

from jsonweb.encode import to_object
from jsonweb.decode import from_object

@from_object()
@to_object()
class User2Group(Base):
	'''
	A link table for many to many on users and groups
	'''

	__tablename__ = 'user2group'
	id         = Column(Integer, primary_key=True)
	user_id    = Column(Integer, ForeignKey('user.id'))
	group_id   = Column(Integer, ForeignKey('group.id'))
	user       = relationship('User', uselist=False, foreign_keys=[user_id], back_populates='groups')
	group      = relationship('Group', uselist=False, foreign_keys=[group_id], back_populates='users')

	def __init__(
		self,
		id=None,
		user_id=None,
		user=None,
		group_id=None,
		group=None
	):
		self.user_id = user_id
		if user:
			self.user = user
			self.user_id = user.id
		self.group_id = group_id
		if group:
			self.group = group
			self.group_id = group.id
		return

	def __dir__(self):
		return [
			'user_id',
			'group_id',
		]

