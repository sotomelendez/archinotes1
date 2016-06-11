# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from archinotes_backend.settings import EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT
from archinotes_backend.helpers import build_response
from archinotes_backend.models import StakeholdersTypes
from mongoengine import connect

class ConstraintsTypesResource(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def GET(self, **kwargs):
        try:
            error_message=None
            
            types = list()
            types.append((('technology'), ('Technology')))
            types.append((('business'), ('Business')))
            
            return build_response(json=types,token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

#Dispatchers
cherrypy.tree.mount(ConstraintsTypesResource(), '/configuration/constraints_types', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})