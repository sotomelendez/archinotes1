# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from archinotes_backend.settings import EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT
from archinotes_backend.helpers import build_response, verify_in_data
from pymongo import MongoClient
import random, string

class DiagramResource(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def GET(self, project_name, viewpoint, **kwargs):
        client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
        db = client[project_name]
        try:
            error_message=None
            results = list(db.diagrams.find({'viewpoint':viewpoint,'deleted':False}))
            if results:
                diagrams = list()
                for result in results:
                    dicts = dict()
                    dicts['name']= result['name']
                    dicts['viewpoint']= result['viewpoint']
                    diagrams.append(dicts)
                return build_response(json=diagrams,token=None)
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
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[data['project_name']]
            db.diagrams.insert({'viewpoint':data['viewpoint'], 'name':data['name'], 'deleted':False})
            return build_response(token=None)
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

    def PUT(self):
        str("")

    def DELETE(self):
        try:
            error_message=None
            data = cherrypy.request.json
            client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
            db = client[project_name]
            diagrams = db.diagrams
            diagrams.update({'viewpoint':data['viewpoint'], 'diagram_name':data['diagram_name']}, { "$set" 'deleted':True},{'upsert':False})

            return ("Diagram %s has been deleted" % data['diagram_name'])
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

#Dispatchers
cherrypy.tree.mount(DiagramResource(), '/editor/diagram', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})
