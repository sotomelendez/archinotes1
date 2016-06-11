
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings

from forms import *
import web_service_connection
import random, json, string

class LazyEncoder(json.JSONEncoder):
    '''Encodes django's lazy i18n strings.
    Used to serialize translated strings to JSON, because
    simplejson chokes on it otherwise. '''
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_unicode(obj)
        return obj

# Create your views here.
def home(request):
    teams = list()
    teams.append(('owned_by_me','owned by me'))
    for i in range(random.randint(1, 10)):
        teams.append((('%s_%s' %('team',i)), ('%s %s' %('team',i))))
    form = WorkspaceForm(teams=teams)
    return render(request, 'mgmt_home.jade', {'form':form})

def get_projects_team(request):
    lista = list()
    for i in range(random.randint(1, 10)):
        dicts = dict()
        dicts['project_name']= '%s_%s' %('project',i)
        dicts['project_description']= '%s_%s' %('description',i)
        lista.append(dicts)
    return HttpResponse(json.dumps({'projects':lista}))

def project(request, name):
    return render(request, 'mgmt_base.jade', {'project_name':name })

def workspace_settings(request):
    return render(request, 'settings.jade', {})

def workspace_help(request):
    return render(request, 'help.jade', {})

def overview(request, name):
    if request.method == 'GET' and name:
        background = "".join( [random.choice(string.letters) for i in xrange(150)] )
        purpose_scope = "".join( [random.choice(string.letters) for i in xrange(100)] )
        overview = "".join( [random.choice(string.letters) for i in xrange(300)] )
        
        #overview_response = web_service_connection.get_overview(project_name=name, request=request)
        
        form = OverviewForm(background=background,purpose_scope=purpose_scope,overview=overview)
        return render(request, 'overview.jade', {'form':form, 'project_name':name})
    elif request.method == 'POST':
        background = request.POST['background']
        purpose_scope = request.POST['purpose_scope']
        overview = request.POST['overview']
        project_name = request.POST['project_name']

        #if background and purpose_scope and overview and project_name
        #    overview_response = web_service_connection.new_overview(background=background, purpose_scope=purpose_scope, overview=overview, project_name=project_name, request=request)

        form = OverviewForm(background=background,purpose_scope=purpose_scope,overview=overview)
        return render(request, 'overview.jade', {'form':form, 'project_name':project_name})

def stakeholders(request, name):
    if request.method == 'GET' and name:
        #stakeholders_types_response = web_service_connection.get_stakeholders_types(request=request)
        stakeholders_types = list()
        stakeholders_types.append((('Architect'), ('Architect')))
        stakeholders_types.append((('Developer'), ('Developer')))
        stakeholders_types.append((('Program_Manager'), ('Program Manager')))

        form = StakeholderForm(stakeholders=stakeholders_types)

        #stakeholders_response = web_service_connection.get_stakeholders(project_name=name, request=request)
        sh = list()
        sh.append('Architect')
        sh.append('Developer')
        sh.append('Program Manager')

        stakeholders = list()
        for i in range(random.randint(0, 10)):
            dicts = dict()
            dicts['role']= '%s_%s' %('role',i)
            dicts['type']= sh[random.randint(0, 2)]
            dicts['concerns']= '%s_%s' %('concerns',i)
            stakeholders.append(dicts)
        return render(request, 'stakeholders.jade', {'project_name':name, 'stakeholders':stakeholders, 'form':form})

@csrf_exempt
def add_stakeholder(request, name):
    if request.method == 'POST' and name:
        role = request.POST['role']
        stakeholder_type = request.POST['stakeholder']
        concerns = request.POST['concerns']

        #if role and stakeholder and overview and concerns
        #    stakeholder_response = web_service_connection.new_stakeholder(role=role, stakeholder_type=stakeholder_type, concerns=concerns, project_name=project_name, request=request)

        return HttpResponse(json.dumps({'message':'success'}, cls=LazyEncoder), content_type='application/json')

def goals(request, name):
    if request.method == 'GET' and name:
        business_goals = list()
        for i in range(random.randint(1, 10)):
            business_goals.append((('%s_%s' %('business_goal',i)), ('%s %s' %('business goal',i))))

        measures = list()
        measures.append((('measure_1'), ('Measure 1')))
        measures.append((('measure_2'), ('Measure 2')))
        measures.append((('measure_3'), ('Measure 3')))
        measures.append((('measure_4'), ('Measure 4')))

        stakeholders_types = list()
        stakeholders_types.append((('Architect'), ('Architect')))
        stakeholders_types.append((('Developer'), ('Developer')))
        stakeholders_types.append((('Program_manager'), ('Program Manager')))

        quality_atributes_types = list()
        quality_atributes_types.append((('Security'), ('Security')))
        quality_atributes_types.append((('Availability'), ('Availability')))
        quality_atributes_types.append((('Modifiability'), ('Modifiability')))

        goal = "".join( [random.choice(string.letters) for i in xrange(70)] )
        objective = "".join( [random.choice(string.letters) for i in xrange(100)] )
        driver = driver = "".join( [random.choice(string.letters) for i in xrange(150)] )

        form = GoalForm(business_goals=business_goals, measures=measures, stakeholders_types=stakeholders_types, quality_atributes_types=quality_atributes_types, goal=goal, objective=objective, driver=driver)
        return render(request, 'goals.jade', {'form':form,'project_name':name,'business_goals':business_goals})
    elif request.method == 'POST':
        project_name = request.POST['project_name']
        name = request.POST['business_goals']
        description = request.POST['goal']
        objective = request.POST['objective']
        driver = request.POST['driver']
        stakeholders = request.POST.getlist('stakeholders')
        quality_atributes = request.POST.getlist('quality_atributes')
        measure = request.POST['measures']

        print 'project_name:',project_name
        print 'name:',name
        print 'description:',description
        print 'objective:',objective
        print 'driver:',driver
        print 'stakeholders:',stakeholders
        print 'quality_atributes:',quality_atributes
        print 'measure:',measure

        return redirect('mgmt:goals', project_name)

def get_business_goal(request, name):
    if request.method == 'GET' and name:
        business_goal_name = request.GET['name']
        #TODO conectar con el backend
        
        measures = list()
        measures.append('Measure 1')
        measures.append('Measure 2')
        measures.append('Measure 3')
        measures.append('Measure 4')

        sh = list()
        sh.append('Architect')
        sh.append('Developer')
        sh.append('Program Manager')

        stakeholders = list()
        stakeholders.append(sh[random.randint(0, 2)])
        stakeholders.append(sh[random.randint(0, 2)])
        
        qa = list()
        qa.append('Security')
        qa.append('Availability')
        qa.append('Modifiability')

        quality_atributes = list()
        quality_atributes.append(qa[random.randint(0, 2)])
        quality_atributes.append(qa[random.randint(0, 2)])

        measure = measures[random.randint(0, 3)]

        goal = "".join( [random.choice(string.letters) for i in xrange(70)] )
        objective = "".join( [random.choice(string.letters) for i in xrange(100)] )
        driver = "".join( [random.choice(string.letters) for i in xrange(150)] )
        
        mini = random.randint(10, 33)
        med = random.randint(10, 33)
        maxi = random.randint(10, 33)

        return HttpResponse(json.dumps({'response':{'goal':goal,'objective':objective,'driver':driver,'stakeholders':stakeholders,'quality_atributes':quality_atributes,'measure':measure,'min':mini,'med':med,'max':maxi}}, cls=LazyEncoder), content_type='application/json')


def constraints(request, name):
    business = list()
    for i in range(random.randint(1, 10)):
        business.append((('%s_%s' %('business',i)), ('%s %s' %('business',i))))

    test = list()
    for i in range(random.randint(1, 10)):
        test.append((('%s_%s' %('technology',i)), ('%s %s' %('technology',i))))
    
    stakeholders = list()
    stakeholders.append((('architect'), ('Architect')))
    stakeholders.append((('developer'), ('Developer')))
    stakeholders.append((('program_manager'), ('Program Manager')))

    types = list()
    types.append((('technology'), ('Technology')))
    types.append((('business'), ('Business')))

    sh = list()
    sh.append('Architect')
    sh.append('Developer')
    sh.append('Program Manager')

    constraint = list()
    constraint.append('Technology')
    constraint.append('Business')

    constraints = list()
    for i in range(random.randint(0, 10)):
        dicts=dict()
        dicts['constraint']= constraint[random.randint(0, 1)]
        dicts['name']="".join( [random.choice(string.letters) for i in xrange(8)] )
        dicts['stakeholder']= sh[random.randint(0, 2)]
        dicts['description']="".join( [random.choice(string.letters) for i in xrange(15)] )
        dicts['alternatives']= "".join( [random.choice(string.letters) for i in xrange(10)] )
        constraints.append(dicts)

    form = ConstraintForm(stakeholders=stakeholders, types=types)
    return render(request, 'constraints.jade', {'form':form, 'project_name':name,'constraints':constraints })

@csrf_exempt
def add_constraint(request, name):
    if request.method == 'POST' and name:
        constraint_name = request.POST['name']
        constaint_type = request.POST['constaint_type']
        stakeholder_type = request.POST['stakeholder_type']
        description = request.POST['description']
        alternatives = request.POST['alternatives']
        print 'constraint_name: ',constraint_name
        print 'constaint_type: ',constaint_type
        print 'stakeholder_type: ',stakeholder_type
        print 'description: ',description
        print 'alternatives: ',alternatives

    return HttpResponse(json.dumps({'message':'success'}, cls=LazyEncoder), content_type='application/json')

def delete_constraint(request, name, constraint_name):
    print 'Project Name: ', name
    print 'Constraint Name: ',  constraint_name
    return redirect('mgmt:constraints', name)

def operations(request, name):
    if request.method == 'GET':
        operational_scenarios = list()
        for i in range(random.randint(1, 10)):
            operational_scenarios.append((('%s_%s' %('Scenario',i)), ('%s %s' %('Scenario',i))))

        inputs = list()
        for i in range(random.randint(1, 4)):
            inputs.append((('%s_%s' %('inputs',i)), ('%s %s' %('inputs',i))))

        outputs = list()
        for i in range(random.randint(1, 4)):
            outputs.append((('%s_%s' %('outputs',i)), ('%s %s' %('outputs',i))))

        stakeholders = list()
        stakeholders.append((('Architect'), ('Architect')))
        stakeholders.append((('Aeveloper'), ('Developer')))
        stakeholders.append((('Program_Manager'), ('Program Manager')))

        stakeholder_description = "".join( [random.choice(string.letters) for i in xrange(50)] )
        functionality = "".join( [random.choice(string.letters) for i in xrange(20)] )
        functionality_description = "".join( [random.choice(string.letters) for i in xrange(150)] )
        context = "".join( [random.choice(string.letters) for i in xrange(20)] )
        context_description = "".join( [random.choice(string.letters) for i in xrange(70)] )

        form = OperationForm(operational_scenarios=operational_scenarios, inputs=inputs, outputs=outputs, stakeholders=stakeholders, stakeholder_description=stakeholder_description, functionality=functionality, functionality_description=functionality_description, context=context, context_description=context_description)

        return render(request, 'operations.jade', {'form':form, 'project_name':name })
    elif request.method == 'POST':
        stakeholder = request.POST['stakeholders']
        stakeholder_description = request.POST['stakeholder_description']
        context = request.POST['context']
        context_description = request.POST['context_description']
        inputs = request.POST.getlist('inputs')
        outputs = request.POST.getlist('outputs')
        functionality = request.POST['functionality']
        functionality_description = request.POST['functionality_description']

        print 'stakeholder: ',stakeholder
        print 'stakeholder_description: ',stakeholder_description
        print 'context: ',context
        print 'context_description: ',context_description
        print 'inputs: ',inputs
        print 'outputs: ',outputs
        print 'functionality: ',functionality
        print 'functionality_description: ',functionality_description

        return redirect('mgmt:operations', name)


def get_operational_scenario(request, name):
    if request.method == 'GET':
        operational_scenario_name = request.GET['name']
        #TODO conectar con el backend
        
        ip = list()
        ip.append('Input 1')
        ip.append('Input 2')
        ip.append('Input 3')
        ip.append('Input 4')

        op = list()
        op.append('Output 1')
        op.append('Output 2')
        op.append('Output 3')
        op.append('Output 4')

        sh = list()
        sh.append('Architect')
        sh.append('Developer')
        sh.append('Program Manager')

        stakeholder = sh[random.randint(0, 2)]
        stakeholder_description = "".join( [random.choice(string.letters) for i in xrange(70)] )
        context = "".join( [random.choice(string.letters) for i in xrange(10)] )
        context_description = "".join( [random.choice(string.letters) for i in xrange(50)] )
        inputs = list()
        inputs.append(ip[random.randint(0, 2)])
        inputs.append(ip[random.randint(0, 2)])
        inputs.append(ip[random.randint(0, 2)])
        outputs = list()
        outputs.append(op[random.randint(0, 2)])
        outputs.append(op[random.randint(0, 2)])
        outputs.append(op[random.randint(0, 2)])
        functionality = "".join( [random.choice(string.letters) for i in xrange(10)] )
        functionality_description = "".join( [random.choice(string.letters) for i in xrange(50)] )

        return HttpResponse(json.dumps({'response':{'stakeholder':stakeholder,'stakeholder_description':stakeholder_description,'context':context,'context_description':context_description,'inputs':inputs,'outputs':outputs,'functionality':functionality,'functionality_description':functionality_description}}, cls=LazyEncoder), content_type='application/json')

def utility_tree(request, name):
    utility_tree_types = list()
    utility_tree_types.append((('SEI'), ('SEI')))
    utility_tree_types.append((('ISO'), ('ISO')))

    utility_tree = list()
    for i in range(random.randint(2, 15)):
        dicts = dict()
        dicts['name']="".join( [random.choice(string.letters) for i in xrange(7)] )
        nodes = list()
        for i in range(random.randint(1, 2)):
            dict_node = dict()
            dict_node['node']="".join( [random.choice(string.letters) for i in xrange(7)] ) 
            a = "".join( [random.choice('HML') for i in xrange(1)])
            b = "".join( [random.choice('HML') for i in xrange(1)])
            dict_node['score']= a + ' ' + b
            nodes.append(dict_node)
        dicts['nodes']=nodes
        utility_tree.append(dicts)

    if random.randint(0, 1) == 1:
        tree = utility_tree
    else:
        tree = list()
    form = UtilityTreeForm(utility_tree_type=utility_tree_types)
    return render(request, 'utility_tree.jade', {'form':form, 'project_name':name, 'utility_tree':tree })

def quality_requirements(request, name):
    quality_atributes = list()
    for i in range(random.randint(2, 5)):
        dicts = dict()
        dicts['name']="".join( [random.choice(string.letters) for i in xrange(7)] )
        a = "".join( [random.choice('HML') for i in xrange(1)])
        b = "".join( [random.choice('HML') for i in xrange(1)])
        if a == 'H':
            dicts['a']='Hight'
        elif a == 'M':
            dicts['a']='Medium'
        else:
            dicts['a']='Low'
        if b == 'H':
            dicts['b']='Hight'
        elif b == 'M':
            dicts['b']='Medium'
        else:
            dicts['b']='Low'
        quality_atributes.append(dicts)
    quality_scenario = list()
    for i in range(random.randint(2, 5)):
        dicts = dict()
        dicts['name']="".join( [random.choice(string.letters) for i in xrange(7)] )
        a = "".join( [random.choice('HML') for i in xrange(1)])
        b = "".join( [random.choice('HML') for i in xrange(1)])
        if a == 'H':
            dicts['a']='Hight'
        elif a == 'M':
            dicts['a']='Medium'
        else:
            dicts['a']='Low'
        if b == 'H':
            dicts['b']='Hight'
        elif b == 'M':
            dicts['b']='Medium'
        else:
            dicts['b']='Low'
        quality_atributes.append(dicts)
    return render(request, 'quality_requirements.jade', {'project_name':name,'quality_atributes':quality_atributes,'quality_scenario':quality_scenario})

def get_quality_attribute_scenarios(request, name):
    if request.method == 'GET':
        #TODO conectar con el backend
        
        queality_scenrios = list()
        for i in range(random.randint(2, 5)):
            dicts=dict()
            dicts['name'] = "".join( [random.choice(string.letters) for i in xrange(10)] )
            dicts['source_of_stimulus'] = "".join( [random.choice(string.letters) for i in xrange(50)] )
            dicts['stimulus'] = "".join( [random.choice(string.letters) for i in xrange(50)] )
            dicts['artifact'] = "".join( [random.choice(string.letters) for i in xrange(50)] )
            dicts['enviroment'] = "".join( [random.choice(string.letters) for i in xrange(50)] )
            dicts['response'] = "".join( [random.choice(string.letters) for i in xrange(50)] )
            dicts['response_measure'] = "".join( [random.choice(string.letters) for i in xrange(50)] )
            queality_scenrios.append(dicts)

        return HttpResponse(json.dumps({'queality_scenrios':queality_scenrios}, cls=LazyEncoder), content_type='application/json')
