# -*- encoding: utf-8 -*-
from django.conf import settings
import datetime
from Archinotes.web_service_config import invoke_web_service, generate_service_url

def list_diagrams(project_name,viewpoint,request):
    try:
        return invoke_web_service('GET', generate_service_url('/editor/diagram', params={'project_name':project_name, 'viewpoint':viewpoint}),request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def new_diagram(project_name,viewpoint,name,request):
    try:
        params = dict()
        if project_name:
            params['project_name'] = project_name
        if viewpoint:
            params['viewpoint'] = viewpoint
        if name:
            params['name'] = name
        return invoke_web_service('POST', generate_service_url('/editor/diagram'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def delete_diagram(project_name,viewpoint,name,request):
    try:
        params = dict()
        if project_name:
            params['project_name'] = project_name
        if viewpoint:
            params['viewpoint'] = viewpoint
        if name:
            params['name'] = name
        return invoke_web_service('DELETE', generate_service_url('/editor/diagram'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_diagram_versions(project_name,viewpoint,name,request):
    try:
        return invoke_web_service('GET', generate_service_url('/editor/diagram_version', params={'project_name':project_name, 'viewpoint':viewpoint, 'diagram_name':name}),request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def new_diagram_version(project_name,viewpoint,name,diagram_version,request):
    try:
        params = dict()
        if project_name:
            params['project_name'] = project_name
        if viewpoint:
            params['viewpoint'] = viewpoint
        if name:
            params['diagram_name'] = name
        if diagram_version:
            params['diagram_version'] = diagram_version
        params['date'] = datetime.date.today().strftime('%d.%m.%Y')
        return invoke_web_service('POST', generate_service_url('/editor/diagram_version'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def add_element(project_name,diagram_name,diagram_version,element_html_id,element_name,element_type,request):
    try:
        params = dict()
        if project_name:
            params['project_name'] = project_name
        if viewpoint:
            params['viewpoint'] = viewpoint
        if diagram_name:
            params['diagram_name'] = diagram_name
        if diagram_version:
            params['diagram_version'] = diagram_version
        if element_html_id:
            params['element_html_id'] = element_html_id
        if element_name:
            params['element_name'] = element_name
        if element_type:
            params['element_type'] = element_type
        return invoke_web_service('POST', generate_service_url('/editor/diagram_element'), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def update_element_position(project_name,diagram_name,diagram_version,element_name,top,left,request):
    try:
        params = dict()
        if project_name:
            params['project_name'] = project_name
        if viewpoint:
            params['viewpoint'] = viewpoint
        if diagram_name:
            params['diagram_name'] = diagram_name
        if diagram_version:
            params['diagram_version'] = diagram_version
        if element_name:
            params['element_name'] = element_nam
        if top:
            params['top'] = top
        if left:
            params['left'] = left
        return invoke_web_service('PUT', generate_service_url('/editor/diagram_element'), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_diagram_elements(project_name,viewpoint,diagram_name,diagram_version,request):
    try:
        return invoke_web_service('GET', generate_service_url('/editor/diagram_element', params={'project_name':project_name, 'viewpoint':viewpoint, 'diagram_name':diagram_name, 'diagram_version':diagram_version}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def delete_element(project_name,diagram_name,diagram_version,element_name,request):
    try:
        params = dict()
        if project_name:
            params['project_name'] = project_name
        if viewpoint:
            params['viewpoint'] = viewpoint
        if diagram_name:
            params['diagram_name'] = diagram_name
        if diagram_version:
            params['diagram_version'] = diagram_version
        if element_name:
            params['element_name'] = element_nam
        return invoke_web_service('DELETE', generate_service_url('/editor/diagram_element'), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def add_connection(project_name,viewpoint,diagram_name,diagram_version,source_html_id,target_html_id,request):
    try:
        params = dict()
        if project_name:
            params['project_name'] = project_name
        if viewpoint:
            params['viewpoint'] = viewpoint
        if diagram_name:
            params['diagram_name'] = diagram_name
        if diagram_version:
            params['diagram_version'] = diagram_version
        if source_name:
            params['source_element_html_id'] = source_name
        if target_name:
            params['target_element_html_id'] = target_name
        return invoke_web_service('POST', generate_service_url('/editor/diagram_connection'), json_data=params,request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}

def list_diagram_connections(project_name,viewpoint,diagram_name,diagram_version,request):
    try:
        return invoke_web_service('GET', generate_service_url('/editor/diagram_connection', params={'project_name':project_name, 'viewpoint':viewpoint, 'diagram_name':diagram_name, 'diagram_version':diagram_version}), request=request)
    except Exception as e:
        return {settings.RESPONSE_MESSAGE:str(e)}
