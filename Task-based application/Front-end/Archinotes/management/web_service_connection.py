# -*- encoding: utf-8 -*-
from django.conf import settings
from Archinotes.web_service_config import invoke_web_service, generate_service_url

def list_stakeholders_types(request):
    try:
        return invoke_web_service('GET', generate_service_url('/configuration/stakeholders_types'), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_measures(request):
    try:
        return invoke_web_service('GET', generate_service_url('/configuration/measures'), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def new_overview(background,purpose_scope,overview,project_name,request):
    try:
        params = dict()
        if background:
            params['background'] = background
        if purpose_scope:
            params['purpose_scope'] = purpose_scope
        if overview:
            params['overview'] = overview
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('POST', generate_service_url('/management/overview'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def get_overview(project_name,request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/overview', params={'project_name':project_name}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def new_stakeholder(role,stakeholder_type,concerns,project_name,request):
    try:
        params = dict()
        if role:
            params['role'] = role
        if stakeholder_type:
            params['stakeholder_type'] = stakeholder_type
        if concerns:
            params['concerns'] = concerns
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('POST', generate_service_url('/management/stakeholder'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def get_stakeholder(role,stakeholder_type,project_name,request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/overview', params={'role':role,'stakeholder_type':stakeholder_type,'project_name':project_name}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_stakeholders(project_name,request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/stakeholder', params={'project_name':project_name}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def new_business_goal(goal,objective,driver,stakeholder,measure,ranges,request):
    try:
        params = dict()
        if goal:
            params['goal'] = goal
        if objective:
            params['objective'] = objective
        if driver:
            params['driver'] = driver
        if stakeholder:
            params['stakeholder'] = stakeholder
        if measure:
            params['measure'] = measure
        if ranges:
            params['ranges'] = ranges
        return invoke_web_service('POST', generate_service_url('/management/business_goal'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def get_business_goal(name,project_name,request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/business_goal', params={'name':name,'project_name':project_name}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_business_goals(project_name,request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/business_goal', params={'project_name':project_name}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def new_constraint(constraint_name,constaint_type,stakeholder_type,description,alternatives,request):
    try:
        params = dict()
        if constraint_name:
            params['constraint_name'] = constraint_name
        if constaint_type:
            params['constaint_type'] = constaint_type
        if stakeholder_type:
            params['stakeholder_type'] = stakeholder_type
        if description:
            params['description'] = description
        if alternatives:
            params['alternatives'] = alternatives
        return invoke_web_service('POST', generate_service_url('/management/constraints'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_constraints(project_name,request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/constraints', params={'project_name':project_name}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def new_operational_scenario(stakeholder,stakeholder_description,context,context_description,inputs,outputs,functionality,functionality_description,request):
    try:
        params = dict()
        if stakeholder:
            params['stakeholder'] = stakeholder
        if stakeholder_description:
            params['stakeholder_description'] = stakeholder_description
        if context:
            params['context'] = context
        if context_description:
            params['context_description'] = context_description
        if inputs:
            params['inputs'] = inputs
        if outputs:
            params['outputs'] = outputs
        if functionality:
            params['functionality'] = functionality
        if functionality_description:
            params['functionality_description'] = functionality_description
        return invoke_web_service('POST', generate_service_url('/management/operational_scenario'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def get_operational_scenario(name,project_name,request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/operational_scenario', params={'name':name,'project_name':project_name}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_operational_scenarios(project_name,request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/operational_scenario', params={'project_name':project_name}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}