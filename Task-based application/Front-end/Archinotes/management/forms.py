#-*- coding: utf-8 -*-
from django import forms

class WorkspaceForm(forms.Form):
    teams = forms.MultipleChoiceField()
    teams.widget.attrs = { 'class' : 'form-control', 'size' : '29' }
    
    def __init__(self, *args, **kwargs):
        teams = kwargs.get('teams', ())
        super(WorkspaceForm, self).__init__(kwargs.get('request', None))
        self.fields['teams'].choices = teams

class OverviewForm(forms.Form):
    background = forms.CharField(widget=forms.Textarea)
    background.widget.attrs = { 'class':'form-control', 'rows':'6', 'style':'resize: none;'}
    purpose_scope = forms.CharField(widget=forms.Textarea)
    purpose_scope.widget.attrs = { 'class':'form-control', 'rows':'6', 'style':'resize: none;' }
    overview = forms.CharField(widget=forms.Textarea)
    overview.widget.attrs = { 'class':'form-control', 'rows':'6', 'style':'resize: none;' }

    def __init__(self, *args, **kwargs):
        background = kwargs.get('background', ())
        purpose_scope = kwargs.get('purpose_scope', ())
        overview = kwargs.get('overview', ())
        super(OverviewForm, self).__init__(kwargs.get('request', None))
        self.fields['background'].initial = background
        self.fields['purpose_scope'].initial = purpose_scope
        self.fields['overview'].initial = overview


class GoalForm(forms.Form):
    name = forms.CharField()
    name.widget.attrs = { 'class':'form-control'}
    business_goals = forms.ChoiceField()
    business_goals.widget.attrs = { 'class' : 'form-control', 'size' : '19' }
    goal = forms.CharField(widget=forms.Textarea)
    goal.widget.attrs = { 'class':'form-control', 'rows':'3', 'style':'resize: none;'}
    objective = forms.CharField(widget=forms.Textarea)
    objective.widget.attrs = { 'class':'form-control', 'rows':'4', 'style':'resize: none;'}
    driver = forms.CharField(widget=forms.Textarea)
    driver.widget.attrs = { 'class':'form-control', 'rows':'4', 'style':'resize: none;'}
    measures = forms.ChoiceField()
    measures.widget.attrs = { 'class' : 'form-control' }
    stakeholders_types = forms.ChoiceField()
    stakeholders_types.widget.attrs = { 'class' : 'form-control' }
    stakeholders = forms.MultipleChoiceField()
    stakeholders.widget.attrs = { 'class' : 'form-control', 'size' : '6'  }
    quality_atributes_types = forms.ChoiceField()
    quality_atributes_types.widget.attrs = { 'class' : 'form-control' }
    quality_atributes = forms.MultipleChoiceField()
    quality_atributes.widget.attrs = { 'class' : 'form-control', 'size' : '6'  }
    
    def __init__(self, *args, **kwargs):
        business_goals = kwargs.get('business_goals', ())
        goal = kwargs.get('goal', ())
        objective = kwargs.get('objective', ())
        driver = kwargs.get('driver', ())
        measures = kwargs.get('measures', ())
        stakeholders_types = kwargs.get('stakeholders_types', ())
        stakeholders = kwargs.get('stakeholders', ())
        quality_atributes_types = kwargs.get('quality_atributes_types', ())
        quality_atributes = kwargs.get('quality_atributes', ())

        super(GoalForm, self).__init__(kwargs.get('request', None))
        self.fields['business_goals'].choices = business_goals
        self.fields['measures'].choices = measures
        self.fields['stakeholders_types'].choices = stakeholders_types
        self.fields['stakeholders'].choices = stakeholders
        self.fields['quality_atributes_types'].choices = quality_atributes_types
        self.fields['quality_atributes'].choices = quality_atributes        
        self.fields['goal'].initial = goal
        self.fields['objective'].initial = objective
        self.fields['driver'].initial = driver

class ConstraintForm(forms.Form):
    stakeholders = forms.ChoiceField()
    stakeholders.widget.attrs = { 'class' : 'form-control' }
    types = forms.ChoiceField()
    types.widget.attrs = { 'class' : 'form-control' }
    name = forms.CharField()
    name.widget.attrs = { 'class' : 'form-control' }
    description = forms.CharField(widget=forms.Textarea)
    description.widget.attrs = {'class':'form-control', 'rows':'3', 'style':'resize: none;'}
    alternatives = forms.CharField(widget=forms.Textarea)
    alternatives.widget.attrs = {'class':'form-control', 'rows':'3', 'style':'resize: none;'}
    def __init__(self, *args, **kwargs):
        stakeholders = kwargs.get('stakeholders', ())
        types = kwargs.get('types', ())
        super(ConstraintForm, self).__init__(kwargs.get('request', None))
        self.fields['stakeholders'].choices = stakeholders
        self.fields['types'].choices = types


class OperationForm(forms.Form):
    name = forms.CharField()
    name.widget.attrs = { 'class':'form-control'}
    operational_scenarios = forms.ChoiceField()
    operational_scenarios.widget.attrs = { 'class' : 'form-control', 'size' : '19' }
    input_name = forms.CharField()
    input_name.widget.attrs = { 'class':'form-control', 'placeholder':'System input', 'style':'width:80%;'} 
    inputs = forms.MultipleChoiceField()
    inputs.widget.attrs = { 'class' : 'form-control', 'size' : '5' }
    output_name = forms.CharField()
    output_name.widget.attrs = { 'class':'form-control', 'placeholder':'System output', 'style':'width:80%;'} 
    outputs = forms.MultipleChoiceField()
    outputs.widget.attrs = { 'class' : 'form-control', 'size' : '5' }
    stakeholders = forms.ChoiceField()
    stakeholders.widget.attrs = { 'class' : 'form-control' }
    stakeholder_description = forms.CharField(widget=forms.Textarea)
    stakeholder_description.widget.attrs = {'class':'form-control', 'rows':'4', 'style':'resize: none;', 'placeholder':'Who or what uses the output and its purpose'}
    functionality = forms.CharField()
    functionality.widget.attrs = { 'class':'form-control', 'placeholder':'Functionality'}
    functionality_description = forms.CharField(widget=forms.Textarea)
    functionality_description.widget.attrs = {'class':'form-control', 'rows':'4', 'style':'resize: none;', 'placeholder':'Description of the current functionality and what the stakeholder hopes'}
    context = forms.CharField()
    context.widget.attrs = { 'class':'form-control', 'placeholder':'Context of the operation'}
    context_description = forms.CharField(widget=forms.Textarea)
    context_description.widget.attrs = {'class':'form-control', 'rows':'4', 'style':'resize: none;', 'placeholder':'What the system does'}  

    def __init__(self, *args, **kwargs):
        operational_scenarios = kwargs.get('operational_scenarios', ())
        inputs = kwargs.get('inputs', ())
        outputs = kwargs.get('outputs', ())
        stakeholders = kwargs.get('stakeholders', ())
        stakeholder_description = kwargs.get('stakeholder_description', ())
        functionality = kwargs.get('functionality', ())
        functionality_description = kwargs.get('functionality_description', ())
        context = kwargs.get('context', ())
        context_description = kwargs.get('context_description', ())
        super(OperationForm, self).__init__(kwargs.get('request', None))
        self.fields['operational_scenarios'].choices = operational_scenarios
        self.fields['inputs'].choices = inputs
        self.fields['outputs'].choices = outputs 
        self.fields['stakeholders'].choices = stakeholders
        self.fields['stakeholder_description'].initial = stakeholder_description
        self.fields['functionality'].initial = functionality
        self.fields['functionality_description'].initial = functionality_description
        self.fields['context'].initial = context
        self.fields['context_description'].initial = context_description

class StakeholderForm(forms.Form):
    role = forms.CharField()
    role.widget.attrs = { 'class':'form-control'}
    stakeholders = forms.ChoiceField()
    stakeholders.widget.attrs = { 'class' : 'form-control' }
    concern_name = forms.CharField()
    concern_name.widget.attrs = { 'class':'form-control'}
    concerns = forms.MultipleChoiceField()
    concerns.widget.attrs = { 'class' : 'form-control', 'size' : '5' }

    def __init__(self, *args, **kwargs):
        stakeholders = kwargs.get('stakeholders', ())
        super(StakeholderForm, self).__init__(kwargs.get('request', None))
        self.fields['stakeholders'].choices = stakeholders

class UtilityTreeForm(forms.Form):
    utility_tree_type = forms.ChoiceField()
    utility_tree_type.widget.attrs = { 'class' : 'form-control' }

    def __init__(self, *args, **kwargs):
        utility_tree_type = kwargs.get('utility_tree_type', ())
        super(UtilityTreeForm, self).__init__(kwargs.get('request', None))
        self.fields['utility_tree_type'].choices = utility_tree_type

