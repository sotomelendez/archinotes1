from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
import requests

import random, json, string, urllib, urllib2

request_headers = {'Content-Type':'application/json'}

save_new_annotation_type_url = "http://localhost:8080/collaborative/annotationTypeResource"
annotation_url = "http://localhost:8080/collaborative/annotationResource"

def settings(request):
	aa = request.GET.get('q')
	deleted = request.GET.get('y')
	if aa != None:
		try:
			
			data = json.loads(urllib2.urlopen(save_new_annotation_type_url).read())
			#data=json.loads(open('data.json').read())

			stakeholders = list()
			for i in range(random.randint(0, 10)):
				dicts = dict()
				dicts['role']= '%s_%s' %('role',i)
				stakeholders.append(dicts)

			#return HttpResponse(str(json.dumps(data)))
			return render(request, 'col_detailed_settings.jade', {'annotation_types':data, 'annotation_string':str(json.dumps(data)), 'current':aa })
			#return render(request, 'col_settings.jade', { })
		except urllib2.HTTPError, e:
			print "HTTP error: %d" % e.code
		except urllib2.URLError, e:
			print "Network error: %s" % e.reason.args[1]
	elif deleted != None:
		par = {'name': deleted}
		requests.delete(save_new_annotation_type_url,params=par)
		data = json.loads(urllib2.urlopen(save_new_annotation_type_url).read())
		return render(request, 'col_settings.jade', {'annotation_types':data, 'annotation_string':str(json.dumps(data)) })


	else:
		try:
			
			data = json.loads(urllib2.urlopen(save_new_annotation_type_url).read())
			#data=json.loads(open('data.json').read())

			stakeholders = list()
			for i in range(random.randint(0, 10)):
				dicts = dict()
				dicts['role']= '%s_%s' %('role',i)
				stakeholders.append(dicts)

			#return HttpResponse(str(json.dumps(data)))
			return render(request, 'col_settings.jade', {'annotation_types':data, 'annotation_string':str(json.dumps(data)), 'stakeholders':stakeholders })
			#return render(request, 'col_settings.jade', { })
		except urllib2.HTTPError, e:
			print "HTTP error: %d" % e.code
		except urllib2.URLError, e:
			print "Network error: %s" % e.reason.args[1]
	

def create_annotation(request):
	return render(request, 'col_create_annotation.jade', {})

def save_new_annotation_type(request):
	if request.method == 'POST':
		annotationType = {}
		annotationType['name'] = request.POST['nombre_annotation']
		annotationType['description'] = request.POST['descripcion_annotation']
		annotationType['inputs'] = []
		annotationType['inputs'].insert(0,{})
		annotationType['inputs'][0]['input_name'] = request.POST['nombreDeEntrada1']
		annotationType['inputs'][0]['input_type'] = request.POST['tipoDeEntrada1']
		act = request.POST.get('nombreDeEntrada2')
		i = 1
		while act != None:
			annotationType['inputs'].insert(i, {})
			annotationType['inputs'][i]['input_name'] = request.POST['nombreDeEntrada'+str(i+1)]
			annotationType['inputs'][i]['input_type'] = request.POST['tipoDeEntrada'+str(i+1)]
			i+=1
			act = request.POST.get('nombreDeEntrada'+str(i+1))

		data = str(json.dumps(annotationType))
		req = urllib2.Request(save_new_annotation_type_url,data,request_headers)
		response = urllib2.urlopen(req).read()

		try:
			
			data = json.loads(urllib2.urlopen(save_new_annotation_type_url).read())
			#data=json.loads(open('data.json').read())

			stakeholders = list()
			for i in range(random.randint(0, 10)):
				dicts = dict()
				dicts['role']= '%s_%s' %('role',i)
				stakeholders.append(dicts)

			#return HttpResponse(str(json.dumps(data)))
			return render(request, 'col_settings.jade', {'annotation_types':data, 'annotation_string':str(json.dumps(data)), 'stakeholders':stakeholders })
			#return render(request, 'col_settings.jade', { })
		except urllib2.HTTPError, e:
			print "HTTP error: %d" % e.code
		except urllib2.URLError, e:
			print "Network error: %s" % e.reason.args[1]


def get_all_annotation_types(request):
	data = json.loads(urllib2.urlopen(save_new_annotation_type_url).read())
	return HttpResponse(str(json.dumps(data)))

def save_new_annotation(request):
	if request.method == 'POST':
		annotation = {}
		annotation['name_annotation_type'] = request.POST['name_annotation_type']
		annotation['elements'] = request.POST['elements']
		annotation['annotation_data'] = []
		act_val = request.POST.get('val0')
		i = 0
		while act_val != None:
			annotation['annotation_data'].insert(i, {})
			annotation['annotation_data'][i][request.POST['inp'+str(i)]]=request.POST['val'+str(i)]
			i+=1
			act_val = request.POST.get('val'+str(i))

		data = str(json.dumps(annotation))
		req = urllib2.Request(annotation_url,data,request_headers)
		response = urllib2.urlopen(req).read()

		return render(request, 'canvas.jade')

def get_all_annotations(request):
	data = json.loads(urllib2.urlopen(annotation_url).read())
	return HttpResponse(str(json.dumps(data)))

def annotation_details(request):
	return HttpResponse(str(request.GET['q']))
		
	

