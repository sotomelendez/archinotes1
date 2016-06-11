# -*- encoding: utf-8 -*-
import cherrypy
from modules.archinotes_backend.models import User
from modules.archinotes_backend.helpers import build_response

class Signup(object):
	exposed = True

	@cherrypy.tools.json_in()
	@cherrypy.tools.json_out()
	def POST(self):
		error_message=None
		try:
			#data = cherrypy.request.json

			#error_message = verify_in_data(data=data,attrs=['name','lastname','email','password','id_number','document_type_id','role_id'])
			#if error_message:
			#	raise Exception

			'''
			user=User(name='juan',lastname='apellido',email='email@algo.com',password='XohImNooBHFR0OVvjcYpJ3NgPQ1qq73WKhHvch0VQtg=',id_number='231231',document_type_id=1,role_id=1)
			cherrypy.request.db.add(user,'USER')
			return build_response(token='Jmzb6shsmLAMHajh')
			'''
		except Exception:
			if error_message:
				return build_response(error_message=error_message,token='Jmzb6shsmLAMHajh')
			raise cherrypy.HTTPError(500)


#Dispatchers
cherrypy.tree.mount(Signup(), '/signup', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})
