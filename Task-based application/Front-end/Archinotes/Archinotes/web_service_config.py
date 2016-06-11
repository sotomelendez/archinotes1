from django.contrib.auth import SESSION_KEY
from django.conf import settings
from errors import UserTokenError, WsError
import httplib,json

def invoke_web_service(method, function_path, json_data=dict(), request=None, response_token=True):
    if settings.DEBUG:
        conn = httplib.HTTPConnection(settings.BACKEND_HOST,'8001')
    else:
        conn = httplib.HTTPSConnection(settings.BACKEND_HOST)
    headers = settings.RESTFUL_HEADER
    headers[settings.API_KEY_MESSAGE] = settings.API_KEY

    conn.request(method, function_path, json.dumps(json_data), settings.RESTFUL_HEADER)
    response = conn.getresponse()
    if response.status is 200:
        response_data = response.read()
        conn.close()
        response = json.loads(response_data)
        if response_token and settings.USER_TOKEN not in response:
            raise UserTokenError('operation_cancelled')
        if settings.USER_TOKEN in response and request is not None:
            request.session[SESSION_KEY] = response[settings.USER_TOKEN]
            request.user.pk = response[settings.USER_TOKEN]
            del response[settings.USER_TOKEN]
        return response
    else:
        conn.close()
        raise WsError(response.reason)

def generate_service_url(function_path, params=None):
    if not params:
        return function_path
    else:
        path_end = None
        for key, value in params.iteritems():
            if not path_end:
                path_end = '?{0}={1}'.format(key, value)
            else:
                path_end += '&{0}={1}'.format(key, value)
        return function_path + path_end