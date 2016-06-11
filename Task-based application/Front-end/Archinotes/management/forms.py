#-*- coding: utf-8 -*-
from django import forms

class WorkspaceForm(forms.Form):
    teams = forms.ChoiceField()
    teams.widget.attrs = { 'class' : 'form-control', 'size' : '29' }
    
    def __init__(self, *args, **kwargs):
        super(WorkspaceForm, self).__init__(kwargs.get('request', None))
        self.fields['teams'].choices = kwargs.get('teams', list())

class OverviewForm(forms.Form):
    background = forms.CharField(widget=forms.Textarea)
    background.widget.attrs = {'class':'form-control','rows':'6','style':'resize: none;','required': True}
    purpose_scope = forms.CharField(widget=forms.Textarea)
    purpose_scope.widget.attrs = {'class':'form-control','rows':'6','style':'resize: none;','required': True}
    overview = forms.CharField(widget=forms.Textarea)
    overview.widget.attrs = {'class':'form-control','rows':'6','style':'resize: none;','required': True}

    def __init__(self, *args, **kwargs):
        super(OverviewForm, self).__init__(kwargs.get('request', None))
        self.fields['background'].initial = kwargs.get('background', str())
        self.fields['purpose_scope'].initial = kwargs.get('purpose_scope', str())
        self.fields['overview'].initial = kwargs.get('overview', str())

class StakeholderForm(forms.Form):
    name = forms.CharField()
    name.widget.attrs = { 'class':'form-control'}
    stakeholders_types = forms.ChoiceField()
    stakeholders_types.widget.attrs = { 'class' : 'form-control' }
    concern_description = forms.CharField(widget=forms.Textarea)
    concern_description.widget.attrs = {'class':'form-control','rows':'2', 'style':'resize: none;'}
    concerns = forms.MultipleChoiceField()
    concerns.widget.attrs = { 'class' : 'form-control', 'size' : '5' }

    def __init__(self, *args, **kwargs):
        super(StakeholderForm, self).__init__(kwargs.get('request', None))
        self.fields['stakeholders_types'].choices = kwargs.get('stakeholders_types', list())

class GoalForm(forms.Form):
    name = forms.CharField()
    name.widget.attrs = { 'class':'form-control'}
    business_goals = forms.ChoiceField()
    business_goals.widget.attrs = { 'class' : 'form-control', 'size' : '19' }
    goal = forms.CharField(widget=forms.Textarea)
    goal.widget.attrs = { 'class':'form-control', 'rows':'3', 'style':'resize: none;', 'placeholder':'<verb> + <element to measure> + <enfasis area> Example: Increase sales in metropolitan area'}
    objective = forms.CharField(widget=forms.Textarea)
    objective.widget.attrs = { 'class':'form-control', 'rows':'4', 'style':'resize: none;', 'placeholder':'<expected return> + BY + <business activity>. Example: Increase sales by a 15percent by the creation of new stores'}
    driver = forms.CharField(widget=forms.Textarea)
    driver.widget.attrs = { 'class':'form-control', 'rows':'4', 'style':'resize: none;', 'placeholder':'A fact that affects the organization'}
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
    minimum = forms.IntegerField()
    minimum.widget.attrs = { 'class' : 'form-control'}
    maximum = forms.IntegerField()
    maximum.widget.attrs = { 'class' : 'form-control'}
    
    def __init__(self, *args, **kwargs): 
        super(GoalForm, self).__init__(kwargs.get('request', None))
        self.fields['business_goals'].choices = kwargs.get('business_goals', list())
        self.fields['measures'].choices = kwargs.get('measures', list())
        self.fields['stakeholders_types'].choices = kwargs.get('stakeholders_types', list())
        self.fields['stakeholders'].choices = kwargs.get('stakeholders', list())
        self.fields['quality_atributes_types'].choices = kwargs.get('quality_atributes_types', list())
        self.fields['quality_atributes'].choices = kwargs.get('quality_atributes', list())        
        self.fields['goal'].initial = kwargs.get('goal', str())
        self.fields['objective'].initial = kwargs.get('objective', str())
        self.fields['driver'].initial = kwargs.get('driver', str())
        self.fields['minimum'].initial = 0
        self.fields['maximum'].initial = 100

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
        super(ConstraintForm, self).__init__(kwargs.get('request', None))
        self.fields['stakeholders'].choices = kwargs.get('stakeholders', list())
        self.fields['types'].choices = kwargs.get('types', list())


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
        super(OperationForm, self).__init__(kwargs.get('request', None))
        self.fields['operational_scenarios'].choices = kwargs.get('operational_scenarios', list())
        self.fields['inputs'].choices = kwargs.get('inputs', list())
        self.fields['outputs'].choices = kwargs.get('outputs', list()) 
        self.fields['stakeholders'].choices = kwargs.get('stakeholders', list())
        self.fields['stakeholder_description'].initial = kwargs.get('stakeholder_description', str())
        self.fields['functionality'].initial = kwargs.get('functionality', str())
        self.fields['functionality_description'].initial = kwargs.get('functionality_description', str())
        self.fields['context'].initial = kwargs.get('context', str())
        self.fields['context_description'].initial = kwargs.get('context_description', str())

class UtilityTreeForm(forms.Form):
    utility_tree_type = forms.ChoiceField()
    utility_tree_type.widget.attrs = { 'class' : 'form-control' }

    def __init__(self, *args, **kwargs):
        super(UtilityTreeForm, self).__init__(kwargs.get('request', None))
        self.fields['utility_tree_type'].choices = kwargs.get('utility_tree_type', list())

