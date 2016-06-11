
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings

from forms import *
import json,random
import web_service_connection

''' helpers '''

class LazyEncoder(json.JSONEncoder):
    '''Encodes django's lazy i18n strings.
    Used to serialize translated strings to JSON, because
    simplejson chokes on it otherwise. '''
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_unicode(obj)
        return obj

''' home '''

def home(request):
    if request.method == 'GET':
        team_response = web_service_connection.list_teams(request=request)
        if team_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            print '\n\n\n',team_response[settings.RESPONSE_CONTENT],'\n\n\n'
            teams = list()
            teams.append(('owned_by_me','owned by me'))
            for team in team_response[settings.RESPONSE_CONTENT]:
                teams.append(((team['name'].replace(' ','_')),(team['name'])))
            form = WorkspaceForm(teams=teams)
            return render(request, 'mgmt_home.jade', {'form':form})
        return render(request, 'mgmt_home.jade', {'error':team_response[settings.RESPONSE_MESSAGE]})

def get_projects_team(request):
    if request.method == 'GET':
        projects_response = web_service_connection.get_projects_team(team=request.GET['team'],request=request)
        if projects_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return HttpResponse(json.dumps({'projects':projects_response[settings.RESPONSE_CONTENT]}))
        return render(request, 'mgmt_home.jade', {'error':projects_response[settings.RESPONSE_MESSAGE]})

def new_project(request):
    if request.method == 'POST':
        projects_response = web_service_connection.new_project(name=request.POST['project_name'],description=request.POST['project_description'],team=request.POST['team'],request=request)
        if projects_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'mgmt_home.jade', {'error':projects_response[settings.RESPONSE_MESSAGE]})

def new_team(request):
    if request.method == 'POST':
        team_response = web_service_connection.new_team(name=request.POST['team_name'],description=request.POST['team_description'],request=request)
        if team_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'mgmt_home.jade', {'error':team_response[settings.RESPONSE_MESSAGE]})

def workspace_settings(request):
    return render(request, 'settings.jade', {})

def workspace_help(request):
    return render(request, 'help.jade', {})

''' overview '''

def overview(request, name):
    if request.method == 'GET' and name:
        overview_response = web_service_connection.get_overview(project_name=name, request=request)
        if overview_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            background = overview_response[settings.RESPONSE_CONTENT]['background']
            purpose_scope = overview_response[settings.RESPONSE_CONTENT]['purpose_scope']
            overview = overview_response[settings.RESPONSE_CONTENT]['overview']
            form = OverviewForm(background=background,purpose_scope=purpose_scope,overview=overview)
            return render(request, 'overview.jade', {'form':form, 'project_name':name})
        else:
            form = OverviewForm()
            return render(request, 'overview.jade', {'form':form, 'project_name':name, 'error':overview_response[settings.RESPONSE_MESSAGE]})
    elif request.method == 'POST':
        background = request.POST['background']
        purpose_scope = request.POST['purpose_scope']
        overview = request.POST['overview']
        project_name = name
        overview_response = web_service_connection.new_overview(background=background, purpose_scope=purpose_scope, overview=overview, project_name=project_name, request=request)
        if overview_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            form = OverviewForm(background=background,purpose_scope=purpose_scope,overview=overview)
            return render(request, 'overview.jade', {'form':form, 'project_name':project_name})
        else:
            form = OverviewForm()
            return render(request, 'overview.jade', {'form':form, 'project_name':name, 'error':overview_response[settings.RESPONSE_MESSAGE]})

''' stakeholders '''

def stakeholders(request, name=None):
    if request.method == 'POST':
        stakeholder_response = web_service_connection.new_stakeholder(name=request.POST['name'], stakeholder_type=request.POST['stakeholders_types'], project_name=request.POST['project_name'], concerns=request.POST.getlist('concerns'), request=request)
        if stakeholder_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        form = StakeholderForm()
        return render(request, 'stakeholders.jade', {'project_name':request.POST['project_name'], 'error':stakeholder_response[settings.RESPONSE_MESSAGE], 'form':form})
    if request.method == 'GET' and name:
        stakeholders_types_response = web_service_connection.list_stakeholders_types(request=request)
        if stakeholders_types_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            form = StakeholderForm(stakeholders_types=stakeholders_types_response[settings.RESPONSE_CONTENT])
        else:
            form = StakeholderForm()
        stakeholders_response = web_service_connection.list_stakeholders(project_name=name, request=request)
        if stakeholders_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return render(request, 'stakeholders.jade', {'project_name':name, 'stakeholders':stakeholders_response[settings.RESPONSE_CONTENT], 'form':form})
        else:
            return render(request, 'stakeholders.jade', {'project_name':name, 'error':stakeholders_response[settings.RESPONSE_MESSAGE], 'form':form})

def get_stakeholder(request, name):
    if request.method == 'GET':
        stakeholder_response = web_service_connection.get_stakeholder(name=request.GET['name'], project_name=request.GET['project_name'], request=request)
        return HttpResponse(json.dumps({stakeholder_response[settings.RESPONSE_MESSAGE]:stakeholder_response[settings.RESPONSE_CONTENT]}, cls=LazyEncoder), content_type='application/json')

def update_stakeholder(request, name):
    if request.method == 'POST':
        stakeholder_response = web_service_connection.update_stakeholder(old_name=request.POST['old_name'], name=request.POST['name'], stakeholder_type=request.POST['stakeholders_types'], project_name=request.POST['project_name'], concerns=request.POST.getlist('concerns'), request=request)
        if stakeholder_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        form = StakeholderForm()
        return render(request, 'stakeholders.jade', {'project_name':request.POST['project_name'], 'error':stakeholder_response[settings.RESPONSE_MESSAGE], 'form':form})

def delete_stakeholder(request, name):
    if request.method == 'POST':
        stakeholder_response = web_service_connection.delete_stakeholder(name=request.POST['name'], project_name=request.POST['project_name'], request=request)
        if stakeholder_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        form = StakeholderForm()
        return render(request, 'stakeholders.jade', {'project_name':request.POST['project_name'], 'error':stakeholder_response[settings.RESPONSE_MESSAGE], 'form':form})

''' goals '''

def goals(request, name=None):
    if request.method == 'GET' and name:
        error = list()
        measures_types_response = web_service_connection.list_measures_types(request=request)
        if measures_types_response[settings.RESPONSE_MESSAGE] != settings.SUCCESS_MESSAGE:
            error.append(measures_types_response[settings.RESPONSE_MESSAGE])
        stakeholders_types_response = web_service_connection.list_stakeholders_types(request=request)
        if stakeholders_types_response[settings.RESPONSE_MESSAGE] != settings.SUCCESS_MESSAGE:
            error.append(stakeholders_types_response[settings.RESPONSE_MESSAGE])
        quality_atributes_types_response = web_service_connection.list_quality_atributes_types(request=request)
        if quality_atributes_types_response[settings.RESPONSE_MESSAGE] != settings.SUCCESS_MESSAGE:
            error.append(quality_atributes_types_response[settings.RESPONSE_MESSAGE])
        business_goals_response = web_service_connection.list_business_goals(project_name=name,request=request)
        if business_goals_response[settings.RESPONSE_MESSAGE] != settings.SUCCESS_MESSAGE:
            error.append(business_goals_response[settings.RESPONSE_MESSAGE])

        if len(error)>0:
            form = GoalForm()
            return render(request, 'goals.jade', {'project_name':name, 'error':error, 'form':form})
        else:
            form = GoalForm(business_goals=business_goals_response[settings.RESPONSE_CONTENT], measures=measures_types_response[settings.RESPONSE_CONTENT], stakeholders_types=stakeholders_types_response[settings.RESPONSE_CONTENT], quality_atributes_types=quality_atributes_types_response[settings.RESPONSE_CONTENT])
            return render(request, 'goals.jade', {'form':form,'project_name':name,'business_goals':business_goals_response[settings.RESPONSE_CONTENT]})

    elif request.method == 'POST':
        business_goal_response = web_service_connection.new_business_goal(name=request.POST['name'], project_name=request.POST['project_name'], request=request)
        if business_goal_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        form = GoalForm()
        return render(request, 'goals.jade', {'project_name':request.POST['project_name'], 'error':business_goal_response[settings.RESPONSE_MESSAGE], 'form':form})

def delete_business_goal(request,name):
    if request.method == 'POST':
        business_goal_response = web_service_connection.delete_business_goal(name=request.POST['name'], project_name=request.POST['project_name'], request=request)
        if business_goal_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        form = GoalForm()
        return render(request, 'goals.jade', {'project_name':request.POST['project_name'], 'error':business_goal_response[settings.RESPONSE_MESSAGE], 'form':form})

def update_business_goal(request,name):
    if request.method == 'POST':
        project_name = request.POST['project_name']
        business_goal_name = request.POST['business_goals']
        goal_description = request.POST['goal']
        objective = request.POST['objective']
        driver = request.POST['driver']
        stakeholders = request.POST.getlist('stakeholders')
        quality_atributes = request.POST.getlist('quality_atributes')
        measure = request.POST['measures']
        chart_min = request.POST['chart_min']
        chart_med = request.POST['chart_med']
        chart_max = request.POST['chart_max']
        range_min = request.POST['minimum']
        range_max = request.POST['maximum']

        business_goal_response = web_service_connection.update_business_goal(name=business_goal_name,goal_description=goal_description,objective=objective,driver=driver,stakeholders=stakeholders,quality_atributes=quality_atributes,measure=measure,project_name=project_name,chart_min=chart_min,chart_med=chart_med,chart_max=chart_max,range_min=range_min,range_max=range_max,request=request)
        if business_goal_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        form = GoalForm()
        return render(request, 'goals.jade', {'project_name':request.POST['project_name'], 'error':business_goal_response[settings.RESPONSE_MESSAGE], 'form':form})

def get_business_goal(request,name):
    if request.method == 'GET':
        business_goal_response = web_service_connection.get_business_goal(name=request.GET['name'], project_name=name, request=request)
        return HttpResponse(json.dumps({business_goal_response[settings.RESPONSE_MESSAGE]:business_goal_response[settings.RESPONSE_CONTENT]}, cls=LazyEncoder), content_type='application/json')

''' constraints '''

def constraints(request, name=None):
    if request.method == 'GET' and name:
        error = list()
        constraints_types_response = web_service_connection.list_constraints_types(request=request)
        if constraints_types_response[settings.RESPONSE_MESSAGE] != settings.SUCCESS_MESSAGE:
            error.append(constraints_types_response[settings.RESPONSE_MESSAGE])
        stakeholders_types_response = web_service_connection.list_stakeholders_types(request=request)
        if stakeholders_types_response[settings.RESPONSE_MESSAGE] != settings.SUCCESS_MESSAGE:
            error.append(stakeholders_types_response[settings.RESPONSE_MESSAGE])
        constraints_response = web_service_connection.list_constraints(project_name=name,request=request)
        if constraints_response[settings.RESPONSE_MESSAGE] != settings.SUCCESS_MESSAGE:
            error.append(constraints_response[settings.RESPONSE_MESSAGE])

        if len(error)>0:
            form = ConstraintForm()
            return render(request, 'constraints.jade', {'project_name':name, 'error':error, 'form':form})
        else:
            form = ConstraintForm(stakeholders=stakeholders_types_response[settings.RESPONSE_CONTENT], types=constraints_types_response[settings.RESPONSE_CONTENT])
            return render(request, 'constraints.jade', {'form':form, 'project_name':name,'constraints':constraints_response[settings.RESPONSE_CONTENT] })

    if request.method == 'POST':
        constraint_response = web_service_connection.new_constraint(name=request.POST['name'], constaint_type=request.POST['types'], stakeholder=request.POST['stakeholders'], description=request.POST['description'], alternatives=request.POST['alternatives'],project_name=request.POST['project_name'], request=request)
        if constraint_response[settings.RESPONSE_MESSAGE]==settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        form = ConstraintForm()
        return render(request, 'constraints.jade', {'project_name':request.POST['project_name'], 'error':constraint_response[settings.RESPONSE_MESSAGE], 'form':form})


def delete_constraint(request, name):
    if request.method == 'POST':
        constraint_response = web_service_connection.delete_constraint(name=request.POST['name'].replace (" ", "_"), project_name=request.POST['project_name'], request=request)
        if constraint_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        form = ConstraintForm()
        return render(request, 'constraints.jade', {'project_name':request.POST['project_name'], 'error':constraint_response[settings.RESPONSE_MESSAGE], 'form':form})

def update_constraint(request, name):
    if request.method == 'POST':
        constraint_response = web_service_connection.update_constraint(old_name=request.POST['old_name'],name=request.POST['name'], constaint_type=request.POST['types'], stakeholder=request.POST['stakeholders'], description=request.POST['description'], alternatives=request.POST['alternatives'],project_name=request.POST['project_name'], request=request)
        if constraint_response[settings.RESPONSE_MESSAGE]==settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        form = ConstraintForm()
        return render(request, 'constraints.jade', {'project_name':request.POST['project_name'], 'error':constraint_response[settings.RESPONSE_MESSAGE], 'form':form})

''' operations '''

def operations(request, name):
    if request.method == 'GET' and name:
        error = list()
        stakeholders_types_response = web_service_connection.list_stakeholders_types(request=request)
        if stakeholders_types_response[settings.RESPONSE_MESSAGE] != settings.SUCCESS_MESSAGE:
            error.append(stakeholders_types_response[settings.RESPONSE_MESSAGE])
        operations_response = web_service_connection.list_operational_scenarios(project_name=name,request=request)
        if operations_response[settings.RESPONSE_MESSAGE] != settings.SUCCESS_MESSAGE:
            error.append(operations_response[settings.RESPONSE_MESSAGE])

        if len(error)>0:
            form = OperationForm()
            return render(request, 'operations.jade', {'project_name':name, 'error':error, 'form':form})
        else:
            form = OperationForm(operational_scenarios=operations_response[settings.RESPONSE_CONTENT], stakeholders=stakeholders_types_response[settings.RESPONSE_CONTENT])
            return render(request, 'operations.jade', {'form':form, 'project_name':name })

    elif request.method == 'POST':
        operations_response = web_service_connection.new_operational_scenario(name=request.POST['name'], project_name=request.POST['project_name'], request=request)
        if operations_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        form = OperationForm()
        return render(request, 'goals.jade', {'project_name':name, 'error':operations_response[settings.RESPONSE_MESSAGE], 'form':form})

def delete_operational_scenario(request,name):
    if request.method == 'POST':
        business_goal_response = web_service_connection.delete_operational_scenario(name=request.POST['name'].replace (" ", "_"), project_name=request.POST['project_name'], request=request)
        if business_goal_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        form = GoalForm()
        return render(request, 'goals.jade', {'project_name':request.POST['project_name'], 'error':business_goal_response[settings.RESPONSE_MESSAGE], 'form':form})

def update_operational_scenario(request, name):
    if request.method == 'POST':
        scenario_name=request.POST['operational_scenarios']
        stakeholder = request.POST['stakeholders']
        stakeholder_description = request.POST['stakeholder_description']
        context = request.POST['context']
        context_description = request.POST['context_description']
        inputs = request.POST.getlist('inputs')
        outputs = request.POST.getlist('outputs')
        functionality = request.POST['functionality']
        functionality_description = request.POST['functionality_description']

        operations_response = web_service_connection.update_operational_scenario(name=scenario_name,stakeholder=stakeholder, stakeholder_description=stakeholder_description, context=context, context_description=context_description, inputs=inputs, outputs=outputs, functionality=functionality, functionality_description=functionality_description, project_name=name, request=request)
        if operations_response[settings.RESPONSE_MESSAGE]==settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        form = OperationForm()
        return render(request, 'operations.jade', {'project_name':name, 'error':operations_response[settings.RESPONSE_MESSAGE], 'form':form})

def get_operational_scenario(request, name):
    if request.method == 'GET':
        operations_response = web_service_connection.get_operational_scenario(name=request.GET['name'], project_name=name, request=request)
        return HttpResponse(json.dumps({operations_response[settings.RESPONSE_MESSAGE]:operations_response[settings.RESPONSE_CONTENT]}, cls=LazyEncoder), content_type='application/json')

''' utility_tree '''

def utility_tree(request, name):
    if request.method == 'POST':
        utility_tree_response = web_service_connection.new_utility_tree(utility_tree_type=request.POST['utility_tree_type'],project_name=name,request=request)
        if utility_tree_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'utility_tree.jade', {'project_name':name, 'error':utility_tree_response[settings.RESPONSE_MESSAGE]})
    if request.method == 'GET':
        utility_tree_response = web_service_connection.get_utility_tree(project_name=name, request=request)
        if utility_tree_response[settings.RESPONSE_MESSAGE]==settings.SUCCESS_MESSAGE:
            utility_tree_types = list()
            utility_tree_types.append((('SEI'), ('SEI')))
            utility_tree_types.append((('ISO'), ('ISO')))
            form = UtilityTreeForm(utility_tree_type=utility_tree_types)
            return render(request, 'utility_tree.jade', {'form':form, 'project_name':name, 'utility_tree':utility_tree_response[settings.RESPONSE_CONTENT] })
        return render(request, 'utility_tree.jade', {'project_name':name, 'error':utility_tree_response[settings.RESPONSE_MESSAGE]})

def update_node_score_utility_tree(request, name):
    if request.method == 'POST':
        qa_node_score =  request.POST['stakeholder_priority'] + ' ' + request.POST['implementation_difficulty']
        utility_tree_response = web_service_connection.update_utility_tree(update_type='qa_node_score',qa_name=request.POST['qa_name'],qa_old_name=None,qa_node_name=request.POST['qa_node_name'],qa_old_node_name=None,qa_node_old_score=request.POST['qa_node_score'],qa_node_score=qa_node_score,project_name=name,request=request)
        if utility_tree_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'utility_tree.jade', {'project_name':name, 'error':utility_tree_response[settings.RESPONSE_MESSAGE]})

def update_node_utility_tree(request, name):
    if request.method == 'POST':
        utility_tree_response = web_service_connection.update_utility_tree(update_type='qa_node',qa_name=request.POST['qa_name'],qa_old_name=None,qa_node_name=request.POST['name'],qa_old_node_name=request.POST['qa_node_name'],qa_node_old_score=None,qa_node_score=None,project_name=name,request=request)
        if utility_tree_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'utility_tree.jade', {'project_name':name, 'error':utility_tree_response[settings.RESPONSE_MESSAGE]})

def delete_node_utility_tree(request, name):
    if request.method == 'POST':
        utility_tree_response = web_service_connection.delete_utility_tree(delete_type='qa_node',qa_name=request.POST['qa_name'],qa_node_name=request.POST['name'],project_name=name,request=request)
        if utility_tree_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'utility_tree.jade', {'project_name':name, 'error':utility_tree_response[settings.RESPONSE_MESSAGE]})

def add_utility_tree(request, name):
    if request.method == 'POST':
        utility_tree_response = web_service_connection.update_utility_tree(update_type='add_qa_name',qa_name=request.POST['quality_attribute_name'],qa_old_name=None,qa_node_name=None,qa_old_node_name=None,qa_node_old_score=None,qa_node_score=None,project_name=name,request=request)
        if utility_tree_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'utility_tree.jade', {'project_name':name, 'error':utility_tree_response[settings.RESPONSE_MESSAGE]})

def add_utility_tree_node(request, name):
    if request.method == 'POST':
        utility_tree_response = web_service_connection.update_utility_tree(update_type='add_qa_node',qa_name=request.POST['old_qa_name'],qa_old_name=None,qa_node_name=request.POST['name_qa'],qa_old_node_name=None,qa_node_old_score=None,qa_node_score=None,project_name=name,request=request)
        if utility_tree_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'utility_tree.jade', {'project_name':name, 'error':utility_tree_response[settings.RESPONSE_MESSAGE]})

def update_utility_tree(request, name):
    if request.method == 'POST':
        utility_tree_response = web_service_connection.update_utility_tree(update_type='qa_name',qa_name=request.POST['name_qa'],qa_old_name=request.POST['old_qa_name'],qa_node_name=None,qa_old_node_name=None,qa_node_old_score=None,qa_node_score=None,project_name=name,request=request)
        if utility_tree_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'utility_tree.jade', {'project_name':name, 'error':utility_tree_response[settings.RESPONSE_MESSAGE]})

def delete_utility_tree(request, name):
    if request.method == 'POST':
        utility_tree_response = web_service_connection.delete_utility_tree(delete_type='qa_name',qa_name=request.POST['name_qa'],qa_node_name=None,project_name=name,request=request)
        if utility_tree_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'utility_tree.jade', {'project_name':name, 'error':utility_tree_response[settings.RESPONSE_MESSAGE]})

''' quality_requirements '''

def quality_requirements(request, name):
    if request.method == 'GET':
        quality_requirements_response = web_service_connection.list_quality_requirements(project_name=name,request=request)
        if quality_requirements_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return render(request, 'quality_requirements.jade', {'project_name':name,'quality_atributes':quality_requirements_response[settings.RESPONSE_CONTENT]})
        return render(request, 'quality_requirements.jade', {'project_name':name, 'error':quality_requirements_response[settings.RESPONSE_MESSAGE]})

    elif request.method == 'POST':
        quality_scenario_response = web_service_connection.new_quality_scenario(quality_atribute=request.POST['quality_atribute'],quality_atribute_node=request.POST['quality_atribute_node'],quality_scenario_name=request.POST['quality_scenario_name'],project_name=name,request=request)
        if quality_scenario_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'quality_requirements.jade', {'project_name':name, 'error':quality_scenario_response[settings.RESPONSE_MESSAGE]})

@csrf_exempt
def update_quality_scenarios(request, name):
    quality_scenario_response = web_service_connection.update_quality_scenario(source=request.POST['source'],stimulus=request.POST['stimulus'],artifact=request.POST['artifact'],enviroment=request.POST['enviroment'],response=request.POST['response'],response_measure=request.POST['response_measure'],quality_scenario_name=request.POST['qs_name'],quality_atribute=request.POST['qa_name'],quality_atribute_node=request.POST['qa_node_name'],project_name=name,request=request)
    if quality_scenario_response[settings.RESPONSE_MESSAGE] == settings.SUCCESS_MESSAGE:
        return redirect(request.META.get('HTTP_REFERER'))
    return render(request, 'quality_requirements.jade', {'project_name':name, 'error':quality_scenario_response[settings.RESPONSE_MESSAGE]})

def get_quality_attribute_scenarios(request, name):
    if request.method == 'GET':
        quality_scenarios_response = web_service_connection.get_quality_scenarios(quality_atribute=request.GET['quality_atribute'], quality_atribute_node=request.GET['quality_atribute_node'], project_name=name, request=request)
        return HttpResponse(json.dumps({quality_scenarios_response[settings.RESPONSE_MESSAGE]:quality_scenarios_response[settings.RESPONSE_CONTENT]}, cls=LazyEncoder), content_type='application/json')
