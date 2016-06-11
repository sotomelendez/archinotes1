# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from forms import *
import web_service_connection
import json

def context(request, name):
    if request.method == 'POST':
        # New diagram
        ins = web_service_connection.new_diagram(project_name=name,viewpoint='Context', name=request.POST['name'], request=request)
        if ins[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            version = web_service_connection.new_diagram_version(project_name=name,viewpoint='Context',name=request.POST['name'], diagram_version='0' ,request=request)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            diag_response = web_service_connection.list_diagrams(project_name=name,viewpoint='Context', request=request)
            if diag_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                return render(request, 'context.jade', {'project_name': name })
    if request.method == 'GET':
        diag_response = web_service_connection.list_diagrams(project_name=name,viewpoint='Context', request=request)
        if diag_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return render(request, 'context.jade', {'project_name': name,'diagrams':diag_response[settings.RESPONSE_CONTENT] })
        else:
            return render(request, 'context.jade', {'project_name': name })

def functional(request, name):
    if request.method == 'POST':
        # New diagram
        ins = web_service_connection.new_diagram(project_name=name,viewpoint='Functional', name=request.POST['name'], request=request)
        if ins[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            version = web_service_connection.new_diagram_version(project_name=name,viewpoint='Functional',name=request.POST['name'],diagram_version='0',request=request)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            diag_response = web_service_connection.list_diagrams(project_name=name,viewpoint='Functional', request=request)
            if diag_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                return render(request, 'functional.jade', {'project_name': name })
    if request.method == 'GET':
        diag_response = web_service_connection.list_diagrams(project_name=name,viewpoint='Functional', request=request)
        if diag_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return render(request, 'functional.jade', {'project_name': name,'diagrams':diag_response[settings.RESPONSE_CONTENT] })
        else:
            return render(request, 'functional.jade', {'project_name': name })

def edit_func(request, name):
    return render(request, 'edit_func.jade', {'project_name': name })

def deployment(request, name):
    if request.method == 'POST':
        # New diagram
        ins = web_service_connection.new_diagram(project_name=name,viewpoint='Deployment', name=request.POST['name'], request=request)
        if ins[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            version = web_service_connection.new_diagram_version(project_name=name,viewpoint='Deployment',name=request.POST['name'],diagram_version='0', request=request)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            diag_response = web_service_connection.list_diagrams(project_name=name,viewpoint='Deployment', request=request)
            if diag_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                return render(request, 'deployment.jade', {'project_name': name })
    if request.method == 'GET':
        diag_response = web_service_connection.list_diagrams(project_name=name,viewpoint='Deployment', request=request)
        if diag_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return render(request, 'deployment.jade', {'project_name': name,'diagrams':diag_response[settings.RESPONSE_CONTENT] })
        else:
            return render(request, 'deployment.jade', {'project_name': name })

def edit_depl(request, name):
    return render(request, 'edit_depl.jade', {'project_name': name })

def information(request, name):
    if request.method == 'POST':
        # New diagram
        ins = web_service_connection.new_diagram(project_name=name,viewpoint='Information', name=request.POST['name'], request=request)
        if ins[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            version = web_service_connection.new_diagram_version(project_name=name,viewpoint='Information',name=request.POST['name'],diagram_version='0', request=request)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            diag_response = web_service_connection.list_diagrams(project_name=name,viewpoint='Information', request=request)
            if diag_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                return render(request, 'information.jade', {'project_name': name })
    if request.method == 'GET':
        diag_response = web_service_connection.list_diagrams(project_name=name,viewpoint='Information', request=request)
        if diag_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return render(request, 'information.jade', {'project_name': name,'diagrams':diag_response[settings.RESPONSE_CONTENT] })
        else:
            return render(request, 'information.jade', {'project_name': name })

def edit_info(request, name):
    return render(request, 'edit_info.jade', {'project_name': name })

def concurrency(request, name):
    if request.method == 'POST':
        # New diagram
        ins = web_service_connection.new_diagram(project_name=name,viewpoint='Concurrency', name=request.POST['name'], request=request)
        if ins[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            version = web_service_connection.new_diagram_version(project_name=name,viewpoint='Concurrency',name=request.POST['name'],diagram_version='0', request=request)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            diag_response = web_service_connection.list_diagrams(project_name=name,viewpoint='Concurrency', request=request)
            if diag_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                return render(request, 'concurrency.jade', {'project_name': name })
    if request.method == 'GET':
        diag_response = web_service_connection.list_diagrams(project_name=name,viewpoint='Concurrency', request=request)
        if diag_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return render(request, 'concurrency.jade', {'project_name': name,'diagrams':diag_response[settings.RESPONSE_CONTENT] })
        else:
            return render(request, 'concurrency.jade', {'project_name': name })

def development(request, name):
    if request.method == 'POST':
        # New diagram
        ins = web_service_connection.new_diagram(project_name=name,viewpoint='Development', name=request.POST['name'], request=request)
        if ins[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            version = web_service_connection.new_diagram_version(project_name=name,viewpoint='Development',name=request.POST['name'], diagram_version='0', request=request)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            diag_response = web_service_connection.list_diagrams(project_name=name,viewpoint='Development', request=request)
            if diag_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                return render(request, 'development.jade', {'project_name': name })
    if request.method == 'GET':
        diag_response = web_service_connection.list_diagrams(project_name=name,viewpoint='Development', request=request)
        if diag_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return render(request, 'development.jade', {'project_name': name,'diagrams':diag_response[settings.RESPONSE_CONTENT] })
        else:
            return render(request, 'development.jade', {'project_name': name })

def show_diagram_versions(request,name):
    diagram_name = request.POST['diagram_name']
    viewpoint = request.POST['viewpoint']
    diag_response = web_service_connection.list_diagrams(project_name=name,viewpoint=viewpoint, request=request)
    if diag_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
        versions_response = web_service_connection.list_diagram_versions(project_name=name,viewpoint=viewpoint, name=diagram_name, request=request)
        return render(request, 'diagram_versions.jade', {'project_name': name,'viewpoint':viewpoint,'diagrams':diag_response[settings.RESPONSE_CONTENT], 'diag_versions':versions_response[settings.RESPONSE_CONTENT], 'selected_name':diagram_name })
    else:
        return render(request, 'diagram_versions.jade', {'project_name':name, 'viewpoint':viewpoint, 'selected_name':diagram_name })

def canvas(request,name):
    if request.method == 'POST':
        if "add_connection" in request.path:
            ins = web_service_connection.add_connection(viewpoint=request.POST['viewpoint'], diagram_name=request.POST['name'],diagram_version=request.POST['diagram_version'],source_html_id=request.POST['source_id'],target_html_id=request.POST['target_id'],request=request)
            if ins[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
                return redirect(request.META.get('HTTP_REFERER'))
        if "add_element" in request.path:
            ins = web_service_connection.add_element(diagram_name=request.POST['name'], diagram_version=request.POST['diagram_version'], element_html_id=request.POST['element_id'], element_name=request.POST['element_name'], element_type=request.POST['element_type'], request=request)
            if ins[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
                return redirect(request.META.get('HTTP_REFERER'))
        if "diagram" in request.path:
            # New Version
            diagram_name = request.POST['diagram_name']
            viewpoint = request.POST['viewpoint']
            diagram_version = request.POST['diagram_version']
            if not 'connection' in request.META.get('HTTP_REFERER') and not 'element' in request.META.get('HTTP_REFERER'):
                ins = web_service_connection.new_diagram_version(project_name=name,viewpoint=viewpoint, name=diagram_name, diagram_version=diagram_version, request=request)
                diagram_elements = web_service_connection.list_diagram_elements(project_name=name, viewpoint=viewpoint, diagram_name=diagram_name, diagram_version=diagram_version, request=request)
                diagram_connections = web_service_connection.list_diagram_connections(project_name=name, viewpoint=viewpoint, diagram_name=diagram_name, diagram_version=diagram_version, request=request)
                if diagram_elements[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
                    return render(request, 'canvas.jade', {'project_name':name, 'viewpoint':viewpoint, 'diagram_name':diagram_name, 'diagram_version':diagram_version, 'elements':diagram_elements[settings.RESPONSE_CONTENT], 'connections':diagram_connections[settings.RESPONSE_CONTENT]})
                else:
                    return render(request, 'canvas.jade', {'project_name':name, 'viewpoint':viewpoint, 'diagram_name':diagram_name, 'diagram_version':diagram_version})
            else:
                diagram_elements = web_service_connection.list_diagram_elements(project_name=name, viewpoint=viewpoint, diagram_name=diagram_name, diagram_version=diagram_version, request=request)
                diagram_connections = web_service_connection.list_diagram_connections(project_name=name, viewpoint=viewpoint, diagram_name=diagram_name, diagram_version=diagram_version, request=request)
                if diagram_elements[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
                    return render(request, 'canvas.jade', {'project_name':name, 'viewpoint':viewpoint, 'diagram_name':diagram_name, 'diagram_version':diagram_version, 'elements':diagram_elements[settings.RESPONSE_CONTENT], 'connections':diagram_connections[settings.RESPONSE_CONTENT]})
                else:
                    return render(request, 'canvas.jade', {'project_name':name, 'viewpoint':viewpoint, 'diagram_name':diagram_name, 'diagram_version':diagram_version})
    if request.method == 'DELETE':
        ans = web_service_connection.delete_element(diagram_name=request.POST['name'], diagram_version=request.POST['diagram_version'], element_name=request.POST['element_name'], request=request)
        if ans[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
    if request.method == 'PUT':
        upd = web_service_connection.update_element_position(diagram_diagram_name=request.POST['name'],diagram_version=request.POST['diagram_version'],element_name=request.POST['element_name'],top=request.POST['top'],left=request.POST['left'],request=request)
        if upd[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
    if request.method == 'GET':
        diagram_elements = web_service_connection.list_diagram_elements(viewpoint=request.POST['viewpoint'], diagram_name=request.POST['name'], diagram_version=request.POST['diagram_version'], request=request)
        diagram_connections = web_service_connection.list_diagram_connections(viewpoint=request.POST['viewpoint'], diagram_name=request.POST['name'], diagram_version=request.POST['diagram_version'], request=request)
        if diagram_elements[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return render(request, 'canvas.jade', {'project_name': name, 'viewpoint':request.POST['viewpoint'], 'diagram_name': request.POST['name'], 'diagram_version':request.POST['diagram_version'], 'elements':diagram_elements[settings.RESPONSE_CONTENT], 'connections':diagram_connections[settings.RESPONSE_CONTENT]})
        else:
            return render(request, 'canvas.jade', {'project_name': name })
