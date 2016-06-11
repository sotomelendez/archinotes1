# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from pymongo import MongoClient
from archinotes_backend.settings import EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT,EXCEPTION_DATA_NOT_EXISTS
from archinotes_backend.helpers import build_response, verify_in_data

class OverviewResource(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def GET(self, project_name, **kwargs):
        try:
            error_message=None
            if project_name:
                client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                db = client[project_name]
                result = db.overview.find_one()

                if result:
                    response = dict()
                    response['background'] = result['background']
                    response['purpose_scope'] = result['purpose_scope']
                    response['overview'] = result['overview']
                else:
                    response = dict()
                    response['background'] = ''
                    response['purpose_scope'] = ''
                    response['overview'] = ''

                return build_response(json=response,token=None)
            else:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'project_name')
                raise Exception
        except Exception:
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
            error_message = verify_in_data(data=data, attrs=['background','purpose_scope','overview','project_name'])
            if error_message:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'overview')
                raise Exception
    
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[data['project_name']]
            result = db.overview.find_one()

            if not result:
                try:
                    db.overview.insert(dict(background=data['background'],purpose_scope=data['purpose_scope'],overview=data['overview']))
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'new_overview')
                    raise Exception
            else:
                db.overview.update({"_id": result['_id']}, {"$set": dict(background=data['background'],purpose_scope=data['purpose_scope'],overview=data['overview'])})

            return build_response(token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

#Dispatchers
cherrypy.tree.mount(OverviewResource(), '/management/overview', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})