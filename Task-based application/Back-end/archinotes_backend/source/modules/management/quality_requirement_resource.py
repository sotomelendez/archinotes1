# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from archinotes_backend.settings import EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT,EXCEPTION_DATA_NOT_EXISTS
from archinotes_backend.helpers import build_response, verify_in_data
from pymongo import MongoClient

class QualityRequirementResource(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def GET(self, quality_atribute=None, quality_atribute_node=None, project_name=None, **kwargs):
        try:
            error_message=None
            if project_name and quality_atribute and quality_atribute_node:

                result = None
                try:
                    client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                    db = client[project_name]
                    results = db.quality_requirements.find(dict(quality_atribute=quality_atribute,quality_atribute_node=quality_atribute_node))
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR,'quality_requirement')
                    raise Exception
                if results:
                    quality_requirements = list()
                    for result in results:
                        dicts=dict()
                        dicts['quality_atribute']= result['quality_atribute']
                        dicts['quality_atribute_node']= result['quality_atribute_node']
                        score = result['quality_atribute_score'].split(' ')
                        if score[0]  == 'H':
                            dicts['a']='Hight'
                        elif score[0]  == 'M':
                            dicts['a']='Medium'
                        else:
                            dicts['a']='Low'
                        if score[1] == 'H':
                            dicts['b']='Hight'
                        elif score[1] == 'M':
                            dicts['b']='Medium'
                        else:
                            dicts['b']='Low'
                        dicts['quality_scenarios']= result['quality_scenarios']
                        quality_requirements.append(dicts)
                    
                    return build_response(json=quality_requirements,token=None)
                else:
                    return build_response(json=list(),token=None)

            elif project_name and not quality_atribute and not quality_atribute_node:
                result = None
                try:
                    client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                    db = client[project_name]
                    results = list(db.quality_requirements.find())
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR,'quality_requirement')
                    raise Exception
                if results:
                    quality_requirements = list()
                    for result in results:
                        dicts=dict()
                        dicts['quality_atribute']= result['quality_atribute']
                        dicts['quality_atribute_node']= result['quality_atribute_node']
                        score = result['quality_atribute_score'].split(' ')
                        if score[0]  == 'H':
                            dicts['a']='Hight'
                        elif score[0]  == 'M':
                            dicts['a']='Medium'
                        else:
                            dicts['a']='Low'
                        if score[1] == 'H':
                            dicts['b']='Hight'
                        elif score[1] == 'M':
                            dicts['b']='Medium'
                        else:
                            dicts['b']='Low'
                        dicts['quality_scenarios']= result['quality_scenarios']
                        quality_requirements.append(dicts)
                    
                    return build_response(json=quality_requirements,token=None)
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
            error_message=None
            data = cherrypy.request.json
            error_message = verify_in_data(data=data, attrs=['quality_atribute','quality_atribute_node','quality_scenario_name','project_name'])
            if error_message:
                raise Exception
             
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[data['project_name']]
            result = db.quality_requirements.find_one({"quality_atribute_node": data['quality_atribute_node']})  
            if result:
                result['quality_scenarios'].append(dict(name=data['quality_scenario_name'],source=str(),stimulus=str(),artifact=str(),enviroment=str(),response=str(),response_measure=str()))
                db.quality_requirements.update({"_id": result['_id']}, {"$set": dict(quality_scenarios=result['quality_scenarios'])})
            else:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'quality_scenario')
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
    def PUT(self,**kwargs):
        try:
            error_message=None
            data = cherrypy.request.json
            error_message = verify_in_data(data=data, attrs=['source','stimulus','artifact','enviroment','response','response_measure','quality_scenario_name','quality_atribute','quality_atribute_node','project_name'])
            if error_message:
                raise Exception
            
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[data['project_name']]
            result = db.quality_requirements.find_one(dict(quality_atribute=data['quality_atribute'],quality_atribute_node=data['quality_atribute_node']))
            
            if result:
                for quality_scenario in result['quality_scenarios']:
                    if quality_scenario['name'] == data['quality_scenario_name']:
                        quality_scenario['name'] = data['quality_scenario_name']
                        quality_scenario['source'] = data['source']
                        quality_scenario['stimulus'] = data['stimulus']
                        quality_scenario['artifact'] = data['artifact']
                        quality_scenario['enviroment'] = data['enviroment']
                        quality_scenario['response'] = data['response']
                        quality_scenario['response_measure'] = data['response_measure']
                        
                db.quality_requirements.update({"_id": result['_id']}, {"$set": dict(quality_scenarios=result['quality_scenarios'])})
            else:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'quality_scenario')
                raise Exception

            return build_response(token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

#Dispatchers
cherrypy.tree.mount(QualityRequirementResource(), '/management/quality_requirement', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})