# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from archinotes_backend.settings import EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT,EXCEPTION_DATA_NOT_EXISTS,EXCEPTION_DATA_ALREADY_EXISTS
from archinotes_backend.helpers import build_response, verify_in_data
from pymongo import MongoClient

class ConstraintResource(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def GET(self, project_name, **kwargs):
        try:
            error_message=None
            
            result = None
            try:
                client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                db = client[project_name]
                results = list(db.constraints.find())
            except Exception:
                error_message = format(EXCEPTION_PROCESSING_ERROR,'constraint')
                raise Exception
            if results:
                constraints = list()
                for result in results:
                    dicts=dict()
                    dicts['constraint']= result['constaint_type']
                    dicts['name']= result['name']
                    dicts['stakeholder']= result['stakeholder']
                    dicts['description']= result['description']
                    dicts['alternatives']= result['alternatives']
                    constraints.append(dicts)
                return build_response(json=constraints,token=None)
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
            error_message = verify_in_data(data=data, attrs=['project_name','description','stakeholder','alternatives','constaint_type','name'])  
            if error_message:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS,'constraint')
                raise Exception
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[data['project_name']]
            result = db.constraints.find_one({"name": data['name']})
            if not result:
                try:
                    db.constraints.insert(dict(name=data['name'],stakeholder=data['stakeholder'].replace ("_", " "),description=data['description'],alternatives=data['alternatives'],constaint_type=data['constaint_type']))
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'new_constraint')
                    raise Exception
            else:
                error_message = format(EXCEPTION_DATA_ALREADY_EXISTS % 'constraint')
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
                    db.constraints.remove({"name": name.replace ("_", " ")})
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'constraint')
                    raise Exception
                return build_response(token=None)
            else:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'constraint')
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
            error_message = verify_in_data(data=data, attrs=['project_name','description','stakeholder','alternatives','constaint_type','name','old_name'])  
            if error_message:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS,'constraint')
                raise Exception
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[data['project_name']]
            result = db.constraints.find_one({"name": data['old_name']})
            if result:
                try:
                    db.constraints.update({"_id": result['_id']}, {"$set": dict(name=data['name'],stakeholder=data['stakeholder'].replace ("_", " "),description=data['description'],alternatives=data['alternatives'],constaint_type=data['constaint_type'])})
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'update_constraint')
                    raise Exception
            else:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'constraint')
                raise Exception
            return build_response(token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

#Dispatchers
cherrypy.tree.mount(ConstraintResource(), '/management/constraint', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})