# -*- encoding: utf-8 -*-
from django.conf import settings
from Archinotes.web_service_config import invoke_web_service, generate_service_url

def sign_up(email,password,request):
    try:
        return invoke_web_service('POST', generate_service_url('/management/user'), json_data={'email':email,'password':password},request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def sign_in(email,password,request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/user', params={'email':email,'password':password}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}