import cherrypy
import json
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import Binary, Code, json_util
from bson.json_util import dumps
import sys, traceback

class annotationResource:

	exposed = True

	def GET(self, id=None):
		annotations = MongoClient().communication.annotations	
		if id == None:
			return dumps(list(annotations.find({'deleted':False})))
		else:
			try:
				ant = annotations.find_one({'_id': ObjectId(oid=str(id)),'deleted':False })
				return dumps(ant)					
			except:
				return('No annotation with the ID %s :-(' % id)

	def POST(self):
		annotations = MongoClient().communication.annotations
		cl = cherrypy.request.headers['Content-Length']
		rawbody = cherrypy.request.body.read(int(cl))
		body = json.loads(rawbody)
		body['deleted']=False
		id = annotations.insert(body)
		return ('Annotation created with ID %s' % id)


	def PUT(self, id, title=None, artist=None):
		str("")


	def DELETE(self, id):
		annotations = MongoClient().communication.annotations	
		try:
			ant = annotations.find_one({'_id': ObjectId(oid=str(id)) })
			ant['deleted']=True
			annotations.save(ant)
			return ('Annotation with ID %s has been deleted' % id)				
		except:
			return traceback.format_exc()