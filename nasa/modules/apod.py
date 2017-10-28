#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .skeletons.base import Base
from datetime import date
import random

class Apod(Base):
	def __init__(self,key):
		Base.__init__(self,"planetary/apod",key)
		
	def random_date(self):
		start_date = date.today().replace(day=1, month=1,year=2000).toordinal()
		end_date = date.today().toordinal()
		return date.fromordinal(random.randint(start_date, end_date))

	def query(self,date=None,hd=True,random=True):
		params = {"hd":hd}

		if not date and random:
			params.update({"date":self.random_date()})
		elif not date and not random:
			date = ""
		elif date:
			params.update({"date":date})

		return self._request_(params)
