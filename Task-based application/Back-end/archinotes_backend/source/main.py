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
#from modules.management.user_resource import *
from modules.management.overview_resource import *
from modules.management.stakeholder_resource import *
from modules.management.business_goal_resource import *
from modules.management.constraint_resource import *
from modules.management.operational_scenario_resource import *
from modules.management.utility_tree_resource import *
from modules.management.quality_requirement_resource import *
from modules.management.project_resource import *
from modules.management.team_resource import *



''' Configuration Module imports '''
from modules.configuration.stakeholders_types_resource import *
from modules.configuration.quality_atributes_types_resource import *
from modules.configuration.measures_types_resource import *
from modules.configuration.constraints_types_resource import *


''' Communication Module imports '''

''' Editor Module imports '''
# Diagram resource  imports
from modules.editor.diagram_resource import *
# Diagram versions resource  imports
from modules.editor.diagram_version_resource import *
# Diagram elements resource  imports
from modules.editor.diagram_element_resource import *
# Diagram connections resource  imports
from modules.editor.diagram_connection_resource import *


''' Listeners '''


''' Certificates '''

#CherryPyWSGIServer.ssl_certificate ="/root/Certificates/server.key"
#CherryPyWSGIServer.ssl_private_key = "/root/Certificates/server.crt"

''' Inits the server '''

# Sets the configuration files
#cherrypy.config.update(os.path.join(settings.CONFIGURATION_FOLDER, settings.CONFIGURATION_FILE))

# Inits the database
cherrypy.tools.db = MongoTool()

# Inits the redis database
cherrypy.tools.cache = RedisTool()

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




