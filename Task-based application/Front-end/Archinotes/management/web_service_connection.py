# -*- encoding: utf-8 -*-
from django.conf import settings
from Archinotes.web_service_config import invoke_web_service, generate_service_url

def new_project(name,description,team,request):
    try:
        params = dict()
        if name:
            params['name'] = name
        if description:
            params['description'] = description
        if team:
            params['team'] = team
        return invoke_web_service('POST', generate_service_url('/management/project'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def new_team(name,description,request):
    try:
        params = dict()
        if name:
            params['name'] = name
        if description:
            params['description'] = description
        return invoke_web_service('POST', generate_service_url('/management/team'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_teams(request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/team'), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def get_projects_team(team,request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/project', params={'team':team}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_stakeholders_types(request):
    try:
        return invoke_web_service('GET', generate_service_url('/configuration/stakeholders_types'), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_quality_atributes_types(request):
    try:
        return invoke_web_service('GET', generate_service_url('/configuration/quality_atributes_types'), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_measures_types(request):
    try:
        return invoke_web_service('GET', generate_service_url('/configuration/measures_types'), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_constraints_types(request):
    try:
        return invoke_web_service('GET', generate_service_url('/configuration/constraints_types'), request=request)
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

def new_stakeholder(name,stakeholder_type,project_name,concerns,request):
    try:
        params = dict()
        if name:
            params['name'] = name
        if stakeholder_type:
            params['stakeholder_type'] = stakeholder_type
        if concerns:
            params['concerns'] = concerns
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('POST', generate_service_url('/management/stakeholder'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def get_stakeholder(name,project_name,request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/stakeholder', params={'name':name,'project_name':project_name}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def update_stakeholder(old_name,name,stakeholder_type,project_name,concerns,request):
    try:
        params = dict()
        if old_name:
            params['old_name'] = old_name
        if name:
            params['name'] = name
        if stakeholder_type:
            params['stakeholder_type'] = stakeholder_type
        if concerns:
            params['concerns'] = concerns
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('PUT', generate_service_url('/management/stakeholder'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def delete_stakeholder(name,project_name,request):
    try:
        params = dict()
        if name:
            params['name'] = name
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('DELETE', generate_service_url('/management/stakeholder', params=params), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_stakeholders(project_name,request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/stakeholder', params={'project_name':project_name}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def new_business_goal(name,project_name,request):
    try:
        params = dict()
        if name:
            params['name'] = name
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('POST', generate_service_url('/management/business_goal'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def update_business_goal(name,goal_description,objective,driver,stakeholders,quality_atributes,measure,project_name,chart_min,chart_med,chart_max,range_min,range_max,request):
    try:
        params = dict()
        if name:
            params['name'] = name
        if goal_description:
            params['goal_description'] = goal_description
        if objective:
            params['objective'] = objective
        if driver:
            params['driver'] = driver
        if stakeholders:
            params['stakeholders'] = stakeholders
        if quality_atributes:
            params['quality_atributes'] = quality_atributes
        if measure:
            params['measure'] = measure
        if project_name:
            params['project_name'] = project_name
        if chart_min:
            params['chart_min'] = chart_min
        if chart_med:
            params['chart_med'] = chart_med
        if chart_max:
            params['chart_max'] = chart_max
        if range_min:
            params['range_min'] = range_min
        if range_max:
            params['range_max'] = range_max

        return invoke_web_service('PUT', generate_service_url('/management/business_goal'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def get_business_goal(name,project_name,request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/business_goal', params={'name':name,'project_name':project_name}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def delete_business_goal(name,project_name,request):
    try:
        params = dict()
        if name:
            params['name'] = name
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('DELETE', generate_service_url('/management/business_goal', params=params), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_business_goals(project_name,request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/business_goal', params={'project_name':project_name}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def new_constraint(name, constaint_type, stakeholder, description, alternatives,project_name, request):
    try:
        params = dict()
        if name:
            params['name'] = name
        if constaint_type:
            params['constaint_type'] = constaint_type
        if stakeholder:
            params['stakeholder'] = stakeholder
        if description:
            params['description'] = description
        if alternatives:
            params['alternatives'] = alternatives
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('POST', generate_service_url('/management/constraint'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def update_constraint(old_name, name, constaint_type, stakeholder, description, alternatives,project_name, request):
    try:
        params = dict()
        if old_name:
            params['old_name'] = old_name
        if name:
            params['name'] = name
        if constaint_type:
            params['constaint_type'] = constaint_type
        if stakeholder:
            params['stakeholder'] = stakeholder
        if description:
            params['description'] = description
        if alternatives:
            params['alternatives'] = alternatives
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('PUT', generate_service_url('/management/constraint'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def delete_constraint(name,project_name,request):
    try:
        params = dict()
        if name:
            params['name'] = name
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('DELETE', generate_service_url('/management/constraint', params=params), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_constraints(project_name,request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/constraint', params={'project_name':project_name}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def new_operational_scenario(name,project_name,request):
    try:
        params = dict()
        if name:
            params['name'] = name
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('POST', generate_service_url('/management/operational_scenario'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def update_operational_scenario(name,stakeholder,stakeholder_description,context,context_description,inputs,outputs,functionality,functionality_description,project_name,request):
    try:
        params = dict()
        if name:
            params['name'] = name
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
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('PUT', generate_service_url('/management/operational_scenario'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def delete_operational_scenario(name,project_name,request):
    try:
        params = dict()
        if name:
            params['name'] = name
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('DELETE', generate_service_url('/management/operational_scenario', params=params), request=request)
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

def new_utility_tree(utility_tree_type,project_name,request):
    try:
        params = dict()
        if utility_tree_type:
            params['utility_tree_type'] = utility_tree_type
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('POST', generate_service_url('/management/utility_tree'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def update_utility_tree(update_type,qa_name,qa_old_name,qa_node_name,qa_old_node_name,qa_node_old_score,qa_node_score,project_name,request):
    try:
        params = dict()
        if update_type:
            params['update_type'] = update_type
        if qa_name:
            params['qa_name'] = qa_name
        if qa_old_name:
            params['qa_old_name'] = qa_old_name
        if qa_node_name:
            params['qa_node_name'] = qa_node_name
        if qa_old_node_name:
            params['qa_old_node_name'] = qa_old_node_name
        if qa_node_old_score:
            params['qa_node_old_score'] = qa_node_old_score
        if qa_node_score:
            params['qa_node_score'] = qa_node_score
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('PUT', generate_service_url('/management/utility_tree'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def delete_utility_tree(delete_type,qa_name,qa_node_name,project_name,request):
    try:
        params = dict()
        if delete_type:
            params['delete_type'] = delete_type
        if qa_name:
            params['qa_name'] = qa_name
        if qa_node_name:
            params['qa_node_name'] = qa_node_name
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('DELETE', generate_service_url('/management/utility_tree', params=params), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def get_utility_tree(project_name, request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/utility_tree', params={'project_name':project_name}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_quality_requirements(project_name,request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/quality_requirement', params={'project_name':project_name}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def new_quality_scenario(quality_atribute,quality_atribute_node,quality_scenario_name,project_name,request):
    try:
        params = dict()
        if quality_atribute:
            params['quality_atribute'] = quality_atribute
        if quality_atribute_node:
            params['quality_atribute_node'] = quality_atribute_node
        if quality_scenario_name:
            params['quality_scenario_name'] = quality_scenario_name
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('POST', generate_service_url('/management/quality_requirement'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def update_quality_scenario(source,stimulus,artifact,enviroment,response,response_measure,quality_scenario_name,quality_atribute,quality_atribute_node,project_name,request):
    try:
        params = dict()
        if source:
            params['source'] = source
        if stimulus:
            params['stimulus'] = stimulus
        if artifact:
            params['artifact'] = artifact
        if enviroment:
            params['enviroment'] = enviroment
        if response:
            params['response'] = response
        if response_measure:
            params['response_measure'] = response_measure
        if quality_scenario_name:
            params['quality_scenario_name'] = quality_scenario_name
        if quality_atribute:
            params['quality_atribute'] = quality_atribute
        if quality_atribute_node:
            params['quality_atribute_node'] = quality_atribute_node
        if project_name:
            params['project_name'] = project_name
        return invoke_web_service('PUT', generate_service_url('/management/quality_requirement'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def get_quality_scenarios(quality_atribute, quality_atribute_node, project_name, request):
    try:
        return invoke_web_service('GET', generate_service_url('/management/quality_requirement', params={'quality_atribute':quality_atribute,'quality_atribute_node':quality_atribute_node,'project_name':project_name}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

