# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from archinotes_backend.settings import EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT,EXCEPTION_DATA_NOT_EXISTS,EXCEPTION_DATA_ALREADY_EXISTS
from archinotes_backend.helpers import build_response, verify_in_data
from pymongo import MongoClient

class OperationalScenarioResource(object):
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
                    result = db.operational_scenarios.find_one({"name": name.replace ("_", " ")})
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'operational_scenarios')
                    raise Exception
                if result:
                    operational_scenario = dict()
                    operational_scenario['stakeholder']=result['stakeholder']
                    operational_scenario['stakeholder_description']=result['stakeholder_description']
                    operational_scenario['context']=result['context']
                    operational_scenario['context_description']=result['context_description']
                    operational_scenario['inputs']=result['inputs']
                    operational_scenario['outputs']=result['outputs']
                    operational_scenario['functionality']=result['functionality']
                    operational_scenario['functionality_description']=result['functionality_description']
                    return build_response(json=operational_scenario,token=None)
                else:
                    error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'operational_scenarios')
                    raise Exception

            if project_name:
                results = None
                try:
                    client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                    db = client[project_name]
                    results = list(db.operational_scenarios.find())
                except Exception:
                    error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'operational_scenarios')
                    raise Exception
                if results:
                    operational_scenarios = list()
                    for result in results:
                        operational_scenarios.append(((result['name'].replace(" ", "_")), (result['name'])))
                    return build_response(json=operational_scenarios,token=None)
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
            error_message = verify_in_data(data=data, attrs=['project_name','name'])
            if error_message:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS,'operational_scenario')
                raise Exception
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[data['project_name']]
            result = db.operational_scenarios.find_one({"name": data['name']})
            if not result:
                try:
                    db.operational_scenarios.insert(dict(name=data['name'],inputs=list(),stakeholder=str(),context_description=str(),functionality_description=str(),functionality=str(),context=str(),outputs=list(),stakeholder_description=str()))
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'new_operational_scenario')
                    raise Exception
            else:
                error_message = format(EXCEPTION_DATA_ALREADY_EXISTS % 'operational_scenario')
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
                    db.operational_scenarios.remove({"name": name.replace ("_", " ")})
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'operational_scenario')
                    raise Exception
                return build_response(token=None)
            else:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'operational_scenario')
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
            error_message = verify_in_data(data=data, attrs=['name','inputs','stakeholder','context_description','functionality_description','functionality','context','outputs','stakeholder_description','project_name'])
            if error_message:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'operational_scenario')
                raise Exception
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[data['project_name']]
            result = db.operational_scenarios.find_one({"name": data['name'].replace("_", " ")})
            if result:
                try:
                    db.operational_scenarios.update({"_id": result['_id']}, {"$set": dict(name=data['name'].replace("_", " "),inputs=data['inputs'],stakeholder=data['stakeholder'],context_description=data['context_description'],functionality_description=data['functionality_description'],functionality=data['functionality'],context=data['context'],outputs=data['outputs'],stakeholder_description=data['stakeholder_description'])})
                except Exception,e:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'operational_scenario')
                    raise Exception
            else:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'operational_scenario')
                raise Exception
            return build_response(token=None)
        except Exception,e:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

#Dispatchers
cherrypy.tree.mount(OperationalScenarioResource(), '/management/operational_scenario', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})