# -*- coding: utf-8 -*-
import hashlib,base64,uuid,datetime,cherrypy,settings,ast

def api_key_exists(api_key):
    pass

def create_token(**kwargs):
    if kwargs:
        hash_sha = hashlib.sha256()
        hash_sha.update(str(kwargs)+str(uuid.uuid4())+str(datetime.datetime.now()))
        token_hash = hash_sha.digest()
        return base64.b64encode(token_hash)
    else:
        raise Exception('To create a token it must need at least one param')

def get_hash(value):
    hash_sha = hashlib.sha256()
    hash_sha.update(str(value))
    digest = hash_sha.digest()
    return base64.b64encode(digest)


def create_session(user_dict,email=None,old_token=None):

    if not email and not old_token:
        raise Exception('At least one param email or token must be passed')

    # Creates a new pipeline (transaction)
    trans = cherrypy.request.cache.pipeline()

    if old_token:
        values=cherrypy.request.cache.get(old_token)
        if values:
            email=ast.literal_eval(values)['email']
        else:
            raise Exception('User is not log in')

    # Verifies if the user is already log in, if so it deletes the current session
    email_hash=get_hash(email)

    if not old_token:
        old_token=cherrypy.request.cache.get(email_hash)
    
    if old_token:
        trans.delete(email_hash)
        trans.delete(old_token)

    # Creates a new token
    token=create_token(user=user_dict)

    # Sets the values with an expire time
    # token|user_info
    # email (digest) | token            
    trans.setex(token,user_dict,settings.TIME_TO_DELETE_TOKEN)
    trans.setex(get_hash(user_dict['email']),token,settings.TIME_TO_DELETE_TOKEN)

    # Executes the transaction
    trans.execute()

    return token
