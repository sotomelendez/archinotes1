# -*- coding: utf-8 -*-
 
import cherrypy,settings
from mongoengine import connect

class MongoTool(cherrypy.Tool):
    def __init__(self):
        cherrypy.Tool.__init__(self, 'on_start_resource',
                               self.bind_database,
                               priority=20)
 
        self.db = connect('default', alias='default',host=settings.DATABASE_ADDRESS, port=settings.DATABASE_PORT)


    def _setup(self):
        cherrypy.Tool._setup(self)
        cherrypy.request.hooks.attach('on_end_resource',
                                      self.end_request,
                                      priority=80)
 
    def bind_database(self):
        cherrypy.engine.publish('bind', self.db)
        cherrypy.request.db = self.db
 
    def end_request(self):
        self.db.connection.disconnect( )
        cherrypy.request.db = None