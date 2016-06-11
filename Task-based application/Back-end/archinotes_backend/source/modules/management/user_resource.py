# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from archinotes_backend.settings import EXCEPTION_DATA_NOT_EXISTS,EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT
from archinotes_backend.helpers import build_response
from mongoengine import connect
from archinotes_backend.models import User

class UserResource(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def GET(self, id=None, **kwargs):
        try:
            error_message=None
            if id:
                try:
                    pass
                except Exception:
                    error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'user')
                    raise Exception

                # Do something
                return build_response(json={'data':'somedata'},token=None)
            else:
                some_list=list()

                for user in User.objects:
                    print user.to_mongo().__to_dict__
                # Do something
                return build_response(json=some_list,token=None)
        except Exception as e:
            print '<<<<EXCEPTION>>>',e
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def POST(self, **kwargs):
        try:
            data = cherrypy.request.json

            connect('archinotes', alias='archinotes',host=DATABASE_ADDRESS, port=DATABASE_PORT)
            user=User(name=data['name'])
            user.switch_db('archinotes')
            user.save()
            error_message = None
            
            
        except Exception as e:
            print '<<<<<<EXCEPTION >>>>',e
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def DELETE(self, id=None, **kwargs):
        error_message=None
        try:
            if id:
                # Do something
                return build_response(token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def PUT(self,**kwargs):
        error_message = None
        try:
            data = cherrypy.request.json
            # Do something
            return build_response(token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

#Dispatchers
cherrypy.tree.mount(UserResource(), '/management/user', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})