# Create your views here.
from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from forms import *
import random

def context(request, name):
    print 'project name: ', name
    return render(request, 'context.jade', {'project_name': name })

def functional(request, name):
    if request.method == 'GET':
        lista = list()
        for i in range(random.randint(1, 10)):
            dicts = dict()
            dicts['name']= '%s_%s' %('name',i)
            dicts['type']= '%s_%s' %('type',i)
            lista.append(dicts)
        return render(request, 'functional.jade', {'project_name': name, 'stakeholders': lista })

def edit_func(request, name):
    return render(request, 'edit_func.jade', {'project_name': name })

def deployment(request, name):
    return render(request, 'deployment.jade', {'project_name': name })

def edit_depl(request, name):
    return render(request, 'edit_depl.jade', {'project_name': name })

def information(request, name):
    return render(request, 'information.jade', {'project_name': name })

def edit_info(request, name):
    return render(request, 'edit_info.jade', {'project_name': name })

def concurrency(request, name):
    return render(request, 'concurrency.jade', {'project_name': name })

def development(request, name):
    return render(request, 'development.jade', {'project_name': name })

def canvas(request, name):
    return render(request, 'canvas.jade', {'project_name': name })
