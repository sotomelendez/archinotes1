# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from archinotes_backend.settings import EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT,EXCEPTION_DATA_NOT_EXISTS,EXCEPTION_DATA_ALREADY_EXISTS
from archinotes_backend.helpers import build_response, verify_in_data
from pymongo import MongoClient

class TeamResource(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def GET(self, **kwargs):
        try:
            error_message=None
            result = None
            try:
                client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                db = client.teams
                results = list(db.teams.find())
            except Exception:
                error_message = format(EXCEPTION_PROCESSING_ERROR % 'teams')
                raise Exception
            if results:
                teams = list()
                for result in results:
                    dicts = dict()
                    dicts['name']= result['name']
                    dicts['description']= result['description']
                    teams.append(dicts)
                return build_response(json=teams,token=None)
            else:
                return build_response(json=list(),token=None)
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
            error_message = verify_in_data(data=data, attrs=['name','description'])
            if error_message:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'team')
                raise Exception
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client.teams
            result = db.teams.find_one({"name": data['name']})
            if not result:
                try:
                    db.teams.insert(dict(name=data['name'],description=data['description']))
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'new_team')
                    raise Exception
            else:
                error_message = format(EXCEPTION_DATA_ALREADY_EXISTS % 'team')
                raise Exception
            return build_response(token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)


#Dispatchers
cherrypy.tree.mount(TeamResource(), '/management/team', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})