#!/usr/bin/python
#import sys,os.path
#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import cherrypy
#from modules.archinotes_backend import settings
from modules.communication.annotationType_resource import * 
from modules.communication.annotation_resource import * 

# Even when models is not used is necessary it's import, because the system has to read the SA models
#from modules.archinotes_backend import models

# Backend module imports
#from modules.archinotes_backend.persistence import MongoTool
#from modules.archinotes_backend.redis_persistence import RedisTool
#from modules.archinotes_backend.authentication.login_resource import *
#from modules.archinotes_backend.authentication.logout_resource import *
#from modules.archinotes_backend.authentication.signup_resource import *

''' Management Module imports '''

# User resource  imports
#from modules.management.user_resource import *



''' Results Module imports '''


''' Vote Count Module imports '''


''' Voting Table imports '''


''' Listeners '''


''' Certificates '''

#CherryPyWSGIServer.ssl_certificate ="/root/Certificates/server.key"
#CherryPyWSGIServer.ssl_private_key = "/root/Certificates/server.crt"

''' Inits the server '''

# Sets the configuration files
#cherrypy.config.update(os.path.join(settings.CONFIGURATION_FOLDER, settings.CONFIGURATION_FILE))

# Inits the database
#cherrypy.tools.db = MongoTool()

# Inits the redis database
#cherrypy.tools.cache = RedisTool()

# Start the server

if __name__ == '__main__':

    cherrypy.tree.mount(
        annotationTypeResource(), '/collaborative/annotationTypeResource',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.tree.mount(
        annotationResource(), '/collaborative/annotationResource',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()




