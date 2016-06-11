# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from archinotes_backend.settings import EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT,EXCEPTION_DATA_NOT_EXISTS,EXCEPTION_DATA_ALREADY_EXISTS
from archinotes_backend.helpers import build_response, verify_in_data
from pymongo import MongoClient

class StakeholderResource(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def GET(self, name=None, project_name=None, **kwargs):
        try:
            error_message=None
            if name and project_name:
                result = None
                try:
                    client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                    db = client[project_name]
                    result = db.stakeholders.find_one({"name": name.replace ("_", " ")})
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'stakeholder')
                    raise Exception
                if result:
                    dicts = dict()
                    dicts['name']=result['name']
                    dicts['type']= result['stakeholder_type']
                    dicts['concerns'] = result['concerns']
                    return build_response(json=dicts,token=None)
                else:
                    error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'stakeholder')
                    raise Exception
            elif project_name:
                result = None
                try:
                    client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                    db = client[project_name]
                    results = list(db.stakeholders.find())
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'stakeholder')
                    raise Exception
                if results:
                    stakeholders = list()
                    for result in results:
                        dicts = dict()
                        dicts['name']= result['name']
                        dicts['aux']= result['name'].replace (" ", "_")
                        dicts['type']= result['stakeholder_type']
                        dicts['concerns']= result['concerns']
                        stakeholders.append(dicts)
                    return build_response(json=stakeholders,token=None)
                else:
                    return build_response(json=list(),token=None)
            else:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'stakeholder')
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
            error_message = verify_in_data(data=data, attrs=['stakeholder_type','project_name','concerns','name'])
            if error_message:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'stakeholder')
                raise Exception
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[data['project_name']]
            result = db.stakeholders.find_one({"name": data['name']})
            if not result:
                try:
                    db.stakeholders.insert(dict(name=data['name'],stakeholder_type=data['stakeholder_type'].replace ("_", " "),concerns=data['concerns']))
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'new_stakeholder')
                    raise Exception
            else:
                error_message = format(EXCEPTION_DATA_ALREADY_EXISTS % 'stakeholder')
                raise Exception
            return build_response(token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def DELETE(self, name=None, project_name=None, **kwargs):
        error_message=None
        try:
            if name and project_name:
                try:
                    client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                    db = client[project_name]
                    db.stakeholders.remove({"name": name.replace ("_", " ")})
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'stakeholder')
                    raise Exception
                return build_response(token=None)
            else:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'stakeholder')
                raise Exception
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def PUT(self,**kwargs):
        try:
            data = cherrypy.request.json
            error_message = verify_in_data(data=data, attrs=['stakeholder_type','project_name','concerns','name','old_name'])
            if error_message:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'stakeholder')
                raise Exception
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[data['project_name']]
            result = db.stakeholders.find_one({"name": data['old_name']})
            if result:
                try:
                    db.stakeholders.update({"_id": result['_id']}, {"$set": dict(name=data['name'],stakeholder_type=data['stakeholder_type'].replace ("_", " "),concerns=data['concerns'])})
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'new_stakeholder')
                    raise Exception
            else:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'stakeholder')
                raise Exception
            return build_response(token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

#Dispatchers
cherrypy.tree.mount(StakeholderResource(), '/management/stakeholder', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})
