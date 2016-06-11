# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from archinotes_backend.settings import EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT
from archinotes_backend.helpers import build_response
from archinotes_backend.models import StakeholdersTypes
from mongoengine import connect

class QualityAtributesTypesResource(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def GET(self, **kwargs):
        try:
            error_message=None
            
            quality_atributes_types = list()
            quality_atributes_types.append((('Performance'), ('Performance')))
            quality_atributes_types.append((('Security'), ('Security')))
            quality_atributes_types.append((('Interoperability'), ('Interoperability')))
            quality_atributes_types.append((('Modifiability'), ('Modifiability')))
            quality_atributes_types.append((('Testability'), ('Testability')))
            quality_atributes_types.append((('Usability'), ('Usability')))
            
            return build_response(json=quality_atributes_types,token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

#Dispatchers
cherrypy.tree.mount(QualityAtributesTypesResource(), '/configuration/quality_atributes_types', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})