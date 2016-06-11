# -*- coding: utf-8 -*-

import settings

# Builds the response message
def build_response(error_message=None,json=dict(),token=None):
    response=dict(settings.RESPONSE_TEMPLATE)
    if error_message:
        response[settings.MESSAGE]=error_message
    else:
        response['response']=json

    if token:
        response[settings.USER_TOKEN]=token

    return response

''' Verifiers '''

# Verifies if a list of attributes are in a dict
def verify_in_data(data={},attrs=[]):
    not_in_data = [attr for attr in attrs if attr not in data or data[attr] == None]
    if len(not_in_data) > 0:
        return settings.EXCEPTION_DATA_NONE % not_in_data[0]
    return None

