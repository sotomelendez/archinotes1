# -*- coding: utf-8 -*-
import cherrypy,redis  

class RedisTool(cherrypy.Tool):
   
    def __init__(self):
        cherrypy.Tool.__init__(self, 'before_handler', self.bind_session, priority=20)
        self.pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

    def _setup(self):
        cherrypy.Tool._setup(self)
        
    def bind_session(self):
        self.redis=redis.Redis(connection_pool=self.pool)
        cherrypy.request.cache=self.redis


    
