# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('management.views',
    url(r'^$', ('home'), name='home'),
    url(r'^settings/$', ('workspace_settings'), name='settings'),
    url(r'^help/$', ('workspace_help'), name='help'),

    url(r'^get_projects_team/$', ('get_projects_team'), name='get_projects_team'),

    url(r'^(?P<name>[^/]+)/$', ('project'), name='project'),
    url(r'^(?P<name>[^/]+)/overview/$', ('overview'), name='overview'),
    url(r'^(?P<name>[^/]+)/stakeholders/$', ('stakeholders'), name='stakeholders'),
    url(r'^(?P<name>[^/]+)/goals/$', ('goals'), name='goals'),
    url(r'^(?P<name>[^/]+)/constraints/$', ('constraints'), name='constraints'),
    url(r'^(?P<name>[^/]+)/operations/$', ('operations'), name='operations'),
    url(r'^(?P<name>[^/]+)/utility_tree/$', ('utility_tree'), name='utility_tree'),
    url(r'^(?P<name>[^/]+)/quality_requirements/$', ('quality_requirements'), name='quality_requirements'),

    url(r'^(?P<name>[^/]+)/get_business_goal/$', ('get_business_goal'), name='get_business_goal'),
    url(r'^(?P<name>[^/]+)/add_stakeholder/$', ('add_stakeholder'), name='add_stakeholder'),
    url(r'^(?P<name>[^/]+)/delete_constraint/(?P<constraint_name>[^/]+)/$', ('delete_constraint'), name='delete_constraint'),
    url(r'^(?P<name>[^/]+)/add_constraint/$', ('add_constraint'), name='add_constraint'),
    url(r'^(?P<name>[^/]+)/get_operational_scenario/$', ('get_operational_scenario'), name='get_operational_scenario'),
    url(r'^(?P<name>[^/]+)/get_quality_attribute_scenarios/$', ('get_quality_attribute_scenarios'), name='get_quality_attribute_scenarios'),
)