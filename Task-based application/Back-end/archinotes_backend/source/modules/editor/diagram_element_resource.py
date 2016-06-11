# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from archinotes_backend.settings import EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT
from archinotes_backend.helpers import build_response, verify_in_data
from pymongo import MongoClient
import random, string

class DiagramElementResource(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def GET(self, viewpoint, diagram_name, diagram_version):
        client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
        db = client[project_name]
        try:
            error_message=None
            results = list(db.diagram_elements.find({'viewpoint':viewpoint, 'diagram_name':diagram_name, 'diagram_version':diagram_version, 'deleted':False}))
            if results:
                elements = list()
                for result in results:
                    dicts = dict()
                    dicts['element_name']= result['element_name']
                    dicts['element_type']= result['element_type']
                    dicts['element_html_id']= result['element_html_id']
                    dicts['top']= result['top']
                    dicts['left']= result['left']
                    elements.append(dicts)
                return build_response(json=elements,token=None)
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
    def POST(self):
        try:
            error_message=None
            data = cherrypy.request.json
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[project_name]
            diagram_elements = db.diagram_elements
            diagram_elements.insert({'viewpoint':data['viewpoint'], 'diagram_name':data['diagram_name'], 'diagram_version':data['diagram_version'], 'element_name':data['element_name'], 'element_type':data['element_type'], 'element_html_id':data['element_html_id'], 'left':0, 'top':0, 'deleted':False})

            return build_response(token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

    def PUT(self):
        try:
            error_message=None
            data = cherrypy.request.json
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[project_name]
            diagram_elements = db.diagram_elements
            diagram_elements.update({'viewpoint':data['viewpoint'], 'diagram_name':data['diagram_name'], 'diagram_version':data['diagram_version'], 'element_name':data['element_name']}, { "$set" 'top':data['top'], 'left':data['left']},{'upsert':False})
            return build_response(token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

    def DELETE(self):
        try:
            error_message=None
            data = cherrypy.request.json
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[project_name]
            diagram_elements = db.diagram_elements
            diagram_elements.update({'viewpoint':data['viewpoint'], 'diagram_name':data['diagram_name'], 'diagram_version':data['diagram_version'], 'element_html_id':data['element_html_id']}, { "$set" 'deleted':True},{'upsert':False})

            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[project_name]
            diagram_connections = db.diagram_connections
            diagram_connections.update({'viewpoint':data['viewpoint'], 'diagram_name':data['diagram_name'], 'diagram_version':data['diagram_version'], 'target_element_html_id':data['element_html_id']}, { "$set" 'deleted':True},{'upsert':False})
            diagram_connections.update({'viewpoint':data['viewpoint'], 'diagram_name':data['diagram_name'], 'diagram_version':data['diagram_version'], 'element_html_id':data['element_html_id']}, { "$set" 'deleted':True},{'upsert':False})

            return build_response(token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

#Dispatchers
cherrypy.tree.mount(DiagramElementResource(), '/editor/diagram_element', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})
