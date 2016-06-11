# -*- encoding: utf-8 -*-
import cherrypy
from modules.archinotes_backend.helpers import build_response
from modules.archinotes_backend.decorators import decode_params,login_required
from modules.archinotes_backend.tokenizer import get_hash
from modules.archinotes_backend.settings import KWARGS_USER,KWARGS_TOKEN

class Logout(object):
    exposed = True
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    @decode_params
    @login_required
    def POST(self,**kwargs):
        trans = cherrypy.request.cache.pipeline()

        # Deletes the session
        trans.delete(get_hash(kwargs[KWARGS_USER]['email']))
        trans.delete(kwargs[KWARGS_TOKEN])

        trans.execute()
        return build_response()

#Dispatchers
cherrypy.tree.mount(Logout(), '/logout', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})