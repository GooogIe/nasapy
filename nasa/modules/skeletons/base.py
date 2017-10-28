#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,json

class Base():
	def __init__(self,final_url,key="DEMO KEY"):
		self.key = key
		self.base_url = "https://api.nasa.gov/"
		self.full_url = self.base_url+final_url

	def _request_(self,params):
		print(self.full_url)
		params.update({"api_key":self.key})
		return self._parse_response_(requests.get(self.full_url,params=params))
	
	def _parse_response_(self,response):
		return json.loads(response.text)
