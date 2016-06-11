# -*- encoding: utf-8 -*-

import cherrypy,ast


from modules.archinotes_backend.models import User
from modules.archinotes_backend.helpers import build_response, verify_in_data
from modules.archinotes_backend.tokenizer import create_session

from modules.archinotes_backend import settings


class Login(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        try:
            '''
            data = cherrypy.request.json
            error_message = verify_in_data(data=data,attrs=['username','password'])
            if error_message:
                raise Exception
            user=None
            try:
                user=cherrypy.request.db.query(User).filter_by(email=data['username'],password=data['password']).one()
            except Exception:
                error_message=settings.EXCEPTION_USER_NOT_EXISTS    
                raise Exception 

            if user.is_active:
                user_dict=model_to_dict(user,attrs=['name','lastname','email','is_active'])
                user_dict['role']=str(user.role.code)

                token=create_session(user_dict,email=data['username'])

                return build_response(json=user_dict,token=token)
            else:
                return build_response(error_message=settings.EXCEPTION_USER_NOT_ACTIVE)
            '''
        except Exception:
            pass
            '''
            if error_message:
                return build_response(error_message=error_message)
            else:
                raise cherrypy.HTTPError(500)
            '''

class LoggedUser(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        try:
            pass
            '''
            data = cherrypy.request.json
            error_message = verify_in_data(data=data,attrs=['user_token'])

            #if error_message:
             #   raise Exception

            values=ast.literal_eval(cherrypy.request.cache.get(data['user_token']))

            return build_response(json=values,token=data['user_token'])
            '''
        except Exception:
            '''
            if error_message:
                return build_response(error_message=error_message)
            else:
                raise cherrypy.HTTPError(500)
            '''
#Dispatchers
cherrypy.tree.mount(Login(), '/login', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})
cherrypy.tree.mount(LoggedUser(), '/logged_user', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})