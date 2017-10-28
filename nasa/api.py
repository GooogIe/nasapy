#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .modules.apod import Apod

class NASA():
	def __init__(self,key):
		self.key = key
		self._apod_ = Apod(key)

	def apod(self,date=None,hd=True,random=True):
		return self._apod_.query(date,hd,random)
