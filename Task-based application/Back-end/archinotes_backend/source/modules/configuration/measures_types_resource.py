# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from archinotes_backend.settings import EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT
from archinotes_backend.helpers import build_response
from archinotes_backend.models import StakeholdersTypes
from mongoengine import connect

class MeasuresTypesResource(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def GET(self, **kwargs):
        try:
            error_message=None
            
            measures_types = list()
            measures_types.append((('Measure_1'), ('Measure 1')))
            measures_types.append((('Measure_2'), ('Measure 2')))
            measures_types.append((('Measure_3'), ('Measure 3')))
            measures_types.append((('Measure_4'), ('Measure 4')))
            
            return build_response(json=measures_types,token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

#Dispatchers
cherrypy.tree.mount(MeasuresTypesResource(), '/configuration/measures_types', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})