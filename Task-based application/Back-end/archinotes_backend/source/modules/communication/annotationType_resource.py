import cherrypy
import json
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import Binary, Code, json_util
from bson.json_util import dumps
import sys, traceback

class annotationTypeResource:

	exposed = True

	def GET(self, id=None):
		annotationTypes = MongoClient().communication.annotationTypes	
		if id == None:
			return dumps(list(annotationTypes.find({'deleted':False})))
		else:
			try:
				ant = annotationTypes.find_one({'_id': ObjectId(oid=str(id)),'deleted':False })
				return dumps(ant)					
			except:
				return('No annotation type with the ID %s :-(' % id)

	def POST(self):
		annotationTypes = MongoClient().communication.annotationTypes
		cl = cherrypy.request.headers['Content-Length']
		rawbody = cherrypy.request.body.read(int(cl))
		body = json.loads(rawbody)
		body['deleted']=False
		id = annotationTypes.insert(body)
		return ('Annotation type created with ID %s' % id)


	def PUT(self, id, title=None, artist=None):
		if id in annotationTypes:
			annotationType = annotationTypes['id']

			annotationType['title'] = title or annotationType['title']
			annotationType['artist'] = artist or annotationType['artist']

			return('Annotation type with the ID %s has been updated' % id)
		else:
			return('No annotation type with the ID %s :-(' % id)


	def DELETE(self, name):
		annotationTypes = MongoClient().communication.annotationTypes	
		try:
			ant = annotationTypes.find_one({'name':name })
			ant['deleted']=True
			annotationTypes.save(ant)
			return ('Annotation with ID %s has been deleted' % id)				
		except:
			return traceback.format_exc()



