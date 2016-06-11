# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from archinotes_backend.settings import EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT,EXCEPTION_DATA_NOT_EXISTS,EXCEPTION_DATA_ALREADY_EXISTS
from archinotes_backend.helpers import build_response, verify_in_data
from pymongo import MongoClient

class ProjectResource(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def GET(self, team=None, **kwargs):
        try:
            if team:
                error_message=None
                result = None
                try:
                    client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                    db = client.projects
                    results = list(db.projects.find(dict(team=team)))
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'projects')
                    raise Exception
                if results:
                    projects = list()
                    for result in results:
                        dicts = dict()
                        dicts['name']= result['name']
                        dicts['description']= result['description']
                        dicts['team']= result['team']
                        projects.append(dicts)
                    return build_response(json=projects,token=None)
                else:
                    return build_response(json=list(),token=None)
            else:
                error_message=None
                result = None
                try:
                    client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                    db = client.projects
                    results = list(db.projects.find())
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'projects')
                    raise Exception
                if results:
                    projects = list()
                    for result in results:
                        dicts = dict()
                        dicts['name']= result['name']
                        dicts['description']= result['description']
                        dicts['team']= result['team']
                        projects.append(dicts)
                    return build_response(json=projects,token=None)
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
            error_message = verify_in_data(data=data, attrs=['name','description','team'])
            if error_message:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'project')
                raise Exception
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client.projects
            result = db.projects.find_one({"name": data['name']})
            if not result:
                try:
                    db.projects.insert(dict(name=data['name'],description=data['description'],team=data['team']))
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'new_project')
                    raise Exception
            else:
                error_message = format(EXCEPTION_DATA_ALREADY_EXISTS % 'project')
                raise Exception
            return build_response(token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)


#Dispatchers
cherrypy.tree.mount(ProjectResource(), '/management/project', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})