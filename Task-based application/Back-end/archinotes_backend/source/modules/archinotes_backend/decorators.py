# -*- encoding: utf-8 -*-
import cherrypy,base64,settings,ast
from functools import wraps
from settings import API_KEY
from tokenizer import create_session

def decode_params(func):
	def wrapper(*args,**kwargs):
		new_kwargs=dict()
		for key,value in kwargs.iteritems():
			new_kwargs[key]=base64.urlsafe_b64decode(str(value))
		return func(*args,**new_kwargs)
	return wraps(func)(wrapper)

def login_required(func):
	def wrapper(*args,**kwargs):

		# Get headers
		api_key=cherrypy.request.headers['api-key']
		old_token=cherrypy.request.headers[settings.USER_TOKEN]

		# Verifies the API KEY and USER TOKEN are correct
		if api_key != API_KEY:
			raise cherrypy.HTTPError(403)

		user_dict=cherrypy.request.cache.get(old_token)

		if not user_dict:
			raise cherrypy.HTTPError(403)

		user_dict=ast.literal_eval(user_dict)

		# Creates the new token
		token=create_session(user_dict,old_token=old_token)

		# Updates the kwargs values
		kwargs.update({'token':token})
		kwargs.update({'user':user_dict})


		return func(*args,**kwargs)
	return wraps(func)(wrapper)

