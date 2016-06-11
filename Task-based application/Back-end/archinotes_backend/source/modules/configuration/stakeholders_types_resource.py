# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from archinotes_backend.settings import EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT
from archinotes_backend.helpers import build_response
from archinotes_backend.models import StakeholdersTypes
from mongoengine import connect

class StakeholdersTypesResource(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def GET(self, **kwargs):
        try:
            error_message=None
            
            stakeholders_types = list()

            stakeholders_types.append((('Investors'), ('Investors')))
            stakeholders_types.append((('Customers_and_users'), ('Customers and users')))
            stakeholders_types.append((('Employees'), ('Employees')))
            stakeholders_types.append((('Regulatory_authorities_and_governments'), ('Regulatory authorities and governments')))
            stakeholders_types.append((('Partners_and_alliances'), ('Partners and alliances')))
            stakeholders_types.append((('External_entities'), ('External entities')))
            stakeholders_types.append((('Architects'), ('Architects')))
            stakeholders_types.append((('Developers_and_testers'), ('Developers and testers')))
            stakeholders_types.append((('Supply_chain_associates'), ('Supply chain associates')))
            
            return build_response(json=stakeholders_types,token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

#Dispatchers
cherrypy.tree.mount(StakeholdersTypesResource(), '/configuration/stakeholders_types', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})