# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from archinotes_backend.settings import EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT,EXCEPTION_DATA_NOT_EXISTS,EXCEPTION_DATA_ALREADY_EXISTS
from archinotes_backend.helpers import build_response, verify_in_data
from pymongo import MongoClient

class BusinessGoalResource(object):
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
                    result = db.business_goals.find_one({"name": name.replace("_", " ")})
                except Exception,e:
                    print '\n\n\n Exception--',e,'\n\n\n' 
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'business_goals')
                    return build_response(json=dict(),token=None)
                    #raise Exception
                if result:
                    business_goals = dict()
                    business_goals['stakeholders']=result['stakeholders']
                    business_goals['quality_atributes']=result['quality_atributes']
                    business_goals['measure']=result['measure']
                    business_goals['goal_description']=result['goal_description']
                    business_goals['objective']=result['objective']
                    business_goals['driver']=result['driver']
                    business_goals['chart_min']=int(result['chart_min'])
                    business_goals['chart_med']=int(result['chart_med'])
                    business_goals['chart_max']=int(result['chart_max'])
                    business_goals['range_min']=result['range_min']
                    business_goals['range_max']=result['range_max']
                    
                    return build_response(json=business_goals,token=None)
                else:
                    error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'business_goals')
                    raise Exception

            if project_name:
                results = None
                try:
                    client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                    db = client[project_name]
                    results = list(db.business_goals.find())
                except Exception:
                    error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'business_goals')
                    raise Exception
                if results:
                    business_goals = list()
                    for result in results:
                        business_goals.append(((result['name'].replace(" ", "_")), (result['name'])))
                    return build_response(json=business_goals,token=None)
                else:
                    return build_response(json=list(),token=None)
        except Exception,e:
            print '\n\n\n Exception2--',e,'\n\n\n' 
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
                error_message = format(EXCEPTION_DATA_NOT_EXISTS,'business_goal')
                raise Exception
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[data['project_name']]
            result = db.business_goals.find_one({"name": data['name']})
            if not result:
                try:
                    db.business_goals.insert(dict(name=data['name'],goal_description=str(),objective=str(),driver=str(),stakeholders=list(),quality_atributes=list(),measure=str(),chart_min=str('33'),chart_med=str('33'),chart_max=str('33'),range_min=str('0'),range_max=str('100')))
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'new_business_goal')
                    raise Exception
            else:
                error_message = format(EXCEPTION_DATA_ALREADY_EXISTS % 'business_goal')
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
                    db.business_goals.remove({"name": name.replace("_", " ")})
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'business_goal')
                    raise Exception
                return build_response(token=None)
            else:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'business_goal')
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
            error_message = verify_in_data(data=data, attrs=['name','goal_description','objective','driver','stakeholders','quality_atributes','measure','project_name','chart_min','chart_med','chart_max','range_min','range_max'])  
            if error_message:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS,'business_goal')
                raise Exception
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[data['project_name']]
            result = db.business_goals.find_one({"name": data['name']})
            if result:
                try:
                    db.business_goals.update({"_id": result['_id']}, {"$set": dict(name=data['name'],goal_description=data['goal_description'],objective=data['objective'],driver=data['driver'],stakeholders=data['stakeholders'],quality_atributes=data['quality_atributes'],measure=data['measure'].replace("_", " "),chart_min=data['chart_min'],chart_med=data['chart_med'],chart_max=data['chart_max'],range_min=data['range_min'],range_max=data['range_max'])})
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'update_business_goal')
                    raise Exception
            else:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'business_goal')
                raise Exception
            return build_response(token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

#Dispatchers
cherrypy.tree.mount(BusinessGoalResource(), '/management/business_goal', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})