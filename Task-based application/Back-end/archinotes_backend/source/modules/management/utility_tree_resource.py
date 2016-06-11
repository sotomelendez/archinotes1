# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from archinotes_backend.settings import EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT,EXCEPTION_DATA_NOT_EXISTS
from archinotes_backend.helpers import build_response, verify_in_data
from pymongo import MongoClient

class UtilityTreeResource(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def GET(self, project_name, **kwargs):
        try:
            error_message=None

            if project_name:
                result = None
                try:
                    client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                    db = client[project_name]
                    result = db.utility_tree.find_one()
                except Exception:
                    error_message = format(EXCEPTION_PROCESSING_ERROR % 'utility_tree')
                    raise Exception

                if result:
                    return build_response(json=result['utility_tree'],token=None)
                else:
                    return build_response(token=None)
            else:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'utility_tree')
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
            error_message = verify_in_data(data=data, attrs=['utility_tree_type','project_name'])
            if error_message:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'utility_tree')
                raise Exception
    
            utility_tree = list()
            if data['utility_tree_type'] == 'ISO':
                dicts = dict()
                dicts['name']='functionality'
                dicts['nodes']=list()
                dicts['nodes'].append(dict(node='interoperability',score='M L'))
                dicts['nodes'].append(dict(node='security',score='H L'))
                dicts['nodes'].append(dict(node='compliance',score='H L'))
                utility_tree.append(dicts)

                dicts = dict()
                dicts['name']='reliability'
                dicts['nodes']=list()
                dicts['nodes'].append(dict(node='maturity',score='M M'))
                dicts['nodes'].append(dict(node='recoverability',score='L L'))
                utility_tree.append(dicts)

                dicts = dict()
                dicts['name']='usability'
                dicts['nodes']=list()
                dicts['nodes'].append(dict(node='learnability',score='M H'))
                dicts['nodes'].append(dict(node='operability',score='M L'))
                utility_tree.append(dicts)

                dicts = dict()
                dicts['name']='efficiency'
                dicts['nodes']=list()
                dicts['nodes'].append(dict(node='time',score='L L'))
                dicts['nodes'].append(dict(node='resource',score='M L'))
                utility_tree.append(dicts)

                dicts = dict()
                dicts['name']='maintainability'
                dicts['nodes']=list()
                dicts['nodes'].append(dict(node='extensibility',score='L L'))
                utility_tree.append(dicts)


            elif data['utility_tree_type'] == 'SEI':
                dicts = dict()
                dicts['name']='performance'
                dicts['nodes']=list()
                dicts['nodes'].append(dict(node='latency',score='M L'))
                dicts['nodes'].append(dict(node='throughput',score='H L'))
                utility_tree.append(dicts)

                dicts = dict()
                dicts['name']='modifiability'
                dicts['nodes']=list()
                dicts['nodes'].append(dict(node='change-COTS',score='L L'))
                utility_tree.append(dicts)

                dicts = dict()
                dicts['name']='availability'
                dicts['nodes']=list()
                dicts['nodes'].append(dict(node='HW-failures',score='M H'))
                dicts['nodes'].append(dict(node='SW-failures',score='M L'))
                utility_tree.append(dicts)

                dicts = dict()
                dicts['name']='security'
                dicts['nodes']=list()
                dicts['nodes'].append(dict(node='confident',score='L L'))
                dicts['nodes'].append(dict(node='integrity',score='M L'))
                utility_tree.append(dicts)

            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[data['project_name']]

            try:
                db.utility_tree.insert(dict(utility_tree=utility_tree))
            except Exception:
                error_message = format(EXCEPTION_PROCESSING_ERROR % 'new_utility_tree')
                raise Exception

            try:
                for quality_atribute in utility_tree:
                    for node in quality_atribute['nodes']:
                        db.quality_requirements.insert(dict(quality_atribute=quality_atribute['name'],quality_atribute_node=node['node'],quality_atribute_score=node['score'],quality_scenarios=list()))
            except Exception:
                error_message = format(EXCEPTION_PROCESSING_ERROR % 'new_utility_tree')
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
    def DELETE(self, delete_type=None, qa_name=None ,qa_node_name=None, project_name=None, **kwargs):
        error_message=None
        try:
            if delete_type and project_name:
                if delete_type == 'qa_node':
                    client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                    db = client[project_name]
                    result = db.utility_tree.find_one()
                    if result and qa_name and qa_node_name:
                        try:
                            for quality_atribute in result['utility_tree']:
                                if quality_atribute['name'] == qa_name:
                                    for node in quality_atribute['nodes']:
                                        if node['node'] == qa_node_name:
                                            quality_atribute['nodes'].remove(node)
                                            db.quality_requirements.remove({"quality_atribute_node": qa_node_name})

                            db.utility_tree.update({"_id": result['_id']}, {"$set": dict(utility_tree=result['utility_tree'])})
                        except Exception:
                            error_message = format(EXCEPTION_PROCESSING_ERROR % 'update_utility_tree')
                            raise Exception
                        return build_response(token=None)
                    else:
                        error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'utility_tree')
                        raise Exception
                elif delete_type == 'qa_name':
                    client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                    db = client[project_name]
                    result = db.utility_tree.find_one()
                    if result and qa_name:
                        try:
                            for quality_atribute in result['utility_tree']:
                                if quality_atribute['name'] == qa_name:
                                    result['utility_tree'].remove(quality_atribute)
                                    db.quality_requirements.remove({"quality_atribute": qa_name})
                            db.utility_tree.update({"_id": result['_id']}, {"$set": dict(utility_tree=result['utility_tree'])})
                        except Exception:
                            error_message = format(EXCEPTION_PROCESSING_ERROR % 'update_utility_tree')
                            raise Exception
                        return build_response(token=None)
                    else:
                        error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'utility_tree')
                        raise Exception
            else:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'utility_tree')
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
        error_message = None
        try:
            data = cherrypy.request.json
            error_message = verify_in_data(data=data, attrs=['update_type','project_name'])
            if error_message:
                error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'update_type')
                raise Exception
            if data['update_type']=='qa_node_score':
                error_message = verify_in_data(data=data, attrs=['qa_name','qa_node_name','qa_node_old_score','qa_node_score'])
                if error_message:
                    error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'utility_tree')
                    raise Exception

                client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                db = client[data['project_name']]
                result = db.utility_tree.find_one()
                if result:
                    try:
                        for quality_atribute in result['utility_tree']:
                            if quality_atribute['name'] == data['qa_name']:
                                for node in quality_atribute['nodes']:
                                    if node['node'] == data['qa_node_name']:
                                        node['score'] = data['qa_node_score']
                                        db.quality_requirements.update({"quality_atribute_node": data['qa_node_name']}, {"$set":{"quality_atribute_score":data['qa_node_score']}})
                        db.utility_tree.update({"_id": result['_id']}, {"$set": dict(utility_tree=result['utility_tree'])})
                    except Exception:
                        error_message = format(EXCEPTION_PROCESSING_ERROR % 'update_utility_tree')
                        raise Exception
                    return build_response(token=None)
                else:
                    error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'utility_tree')
                    raise Exception
            elif data['update_type']=='qa_node':
                error_message = verify_in_data(data=data, attrs=['qa_name','qa_node_name','qa_old_node_name'])
                if error_message:
                    error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'utility_tree')
                    raise Exception

                client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                db = client[data['project_name']]
                result = db.utility_tree.find_one()
                if result:
                    try:
                        for quality_atribute in result['utility_tree']:
                            if quality_atribute['name'] == data['qa_name']:
                                for node in quality_atribute['nodes']:
                                    if node['node'] == data['qa_old_node_name']:
                                        node['node'] = data['qa_node_name']
                                        db.quality_requirements.update({"quality_atribute_node": data['qa_old_node_name']}, {"$set":{"quality_atribute_node":data['qa_node_name']}})

                        db.utility_tree.update({"_id": result['_id']}, {"$set": dict(utility_tree=result['utility_tree'])})
                    except Exception:
                        error_message = format(EXCEPTION_PROCESSING_ERROR % 'update_utility_tree')
                        raise Exception
                    return build_response(token=None)
                else:
                    error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'utility_tree')
                    raise Exception

            elif data['update_type']=='qa_name':
                error_message = verify_in_data(data=data, attrs=['qa_name','qa_old_name'])
                if error_message:
                    error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'utility_tree')
                    raise Exception

                client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                db = client[data['project_name']]
                result = db.utility_tree.find_one()
                if result:
                    try:
                        for quality_atribute in result['utility_tree']:
                            if quality_atribute['name'] == data['qa_old_name']:
                                quality_atribute['name'] = data['qa_name']
                                db.quality_requirements.update(
                                    {"quality_atribute": data['qa_old_name']},
                                    {"$set":{"quality_atribute":data['qa_name']}},
                                    **{
                                        "upsert":True,
                                        "multi":True
                                    })

                        db.utility_tree.update({"_id": result['_id']}, {"$set": dict(utility_tree=result['utility_tree'])})
                    except Exception:
                        error_message = format(EXCEPTION_PROCESSING_ERROR % 'update_utility_tree')
                        raise Exception
                    return build_response(token=None)
                else:
                    error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'utility_tree')
                    raise Exception

            elif data['update_type']=='add_qa_node':
                error_message = verify_in_data(data=data, attrs=['qa_name','qa_node_name'])
                if error_message:
                    error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'utility_tree')
                    raise Exception

                client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                db = client[data['project_name']]
                result = db.utility_tree.find_one()
                if result:
                    try:
                        for quality_atribute in result['utility_tree']:
                            if quality_atribute['name'] == data['qa_name']:
                                quality_atribute['nodes'].append(dict(node=data['qa_node_name'],score='L L'))
                                db.quality_requirements.insert(dict(quality_atribute=data['qa_name'],quality_atribute_node=data['qa_node_name'],quality_atribute_score='L L',quality_scenarios=list()))

                        db.utility_tree.update({"_id": result['_id']}, {"$set": dict(utility_tree=result['utility_tree'])})
                    except Exception:
                        error_message = format(EXCEPTION_PROCESSING_ERROR % 'update_utility_tree')
                        raise Exception
                    return build_response(token=None)
                else:
                    error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'utility_tree')
                    raise Exception

            elif data['update_type']=='add_qa_name':
                error_message = verify_in_data(data=data, attrs=['qa_name'])
                if error_message:
                    error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'utility_tree')
                    raise Exception

                client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
                db = client[data['project_name']]
                result = db.utility_tree.find_one()
                if result:
                    try:
                        dicts = dict()
                        dicts['name']=data['qa_name']
                        dicts['nodes']=list()
                        dicts['nodes'].append(dict(node=data['qa_name'],score='L L'))
                        result['utility_tree'].append(dicts)

                        db.quality_requirements.insert(dict(quality_atribute=data['qa_name'],quality_atribute_node=data['qa_name'],quality_atribute_score='L L',quality_scenarios=list()))
                        db.utility_tree.update({"_id": result['_id']}, {"$set": dict(utility_tree=result['utility_tree'])})
                    except Exception:
                        error_message = format(EXCEPTION_PROCESSING_ERROR % 'update_utility_tree')
                        raise Exception
                    return build_response(token=None)
                else:
                    error_message = format(EXCEPTION_DATA_NOT_EXISTS % 'utility_tree')
                    raise Exception

            return build_response(token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

#Dispatchers
cherrypy.tree.mount(UtilityTreeResource(), '/management/utility_tree', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})