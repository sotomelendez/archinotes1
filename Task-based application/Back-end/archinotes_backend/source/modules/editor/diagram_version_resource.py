# -*- encoding: utf-8 -*-
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cherrypy
from archinotes_backend.settings import EXCEPTION_PROCESSING_ERROR,DATABASE_ADDRESS,DATABASE_PORT
from archinotes_backend.helpers import build_response, verify_in_data
from pymongo import MongoClient
from datetime import date
import random, string

class DiagramVersionResource(object):
    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    #@decode_params
    #@login_required
    def GET(self, project_name, viewpoint, diagram_name, **kwargs):
        client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
        db = client[project_name]
        try:
            error_message=None
            results = list(db.diagram_versions.find({'viewpoint':viewpoint,'diagram_name':diagram_name,'deleted':False}))
            if results:
                versions = list()
                for result in results:
                    dicts = dict()
                    dicts['viewpoint']= result['viewpoint']
                    dicts['diagram_name']= result['diagram_name']
                    dicts['diagram_version']= result['diagram_version']
                    dicts['date']= result['date']
                    versions.append(dicts)
                return build_response(json=versions,token=None)
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
            db = client[data['project_name']]
            version = db.diagram_versions.count()+1
            db.diagram_versions.insert({'viewpoint':data['viewpoint'], 'diagram_name':data['diagram_name'], 'diagram_version':str(version), 'date':data['date'], 'deleted':False})
            if version > 1:
                # Insert elements from previous version in new one
                diagram_elements = MongoClient().editor.diagram_elements
                diagram_connections = MongoClient().editor.diagram_connections
                elems = list(diagram_elements.find({'viewpoint':data['viewpoint'], 'diagram_name':data['diagram_name'], 'diagram_version':ver, 'deleted':False}))
                cons = list(diagram_connections.find({'viewpoint':data['viewpoint'], 'diagram_name':data['diagram_name'], 'diagram_version':ver, 'deleted':False}))
                for elem in elems:
                    elem['diagram_version'] = version
                    diagram_elements.insert(elem)
                for conn in cons:
                    conn['diagram_version'] = version
                    diagram_connections.insert(conn)
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
            diagram_versions = db.diagram_versions
            diagram_versions.update({'viewpoint':data['viewpoint'], 'diagram_name':data['diagram_name'], 'diagram_version':data['diagram_version']}, { "$set" 'deleted':True},{'upsert':False})

            return ("Diagram %s has been deleted" % data['diagram_name'])
        except Exception:
            if not error_message:
                error_message = EXCEPTION_PROCESSING_ERROR
            return build_response(error_message=error_message,token=None)

#Dispatchers
cherrypy.tree.mount(DiagramVersionResource(), '/editor/diagram_version', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})
