# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('management.views',
    url(r'^$', ('home'), name='home'),

    url(r'^/get_projects_team/$', ('get_projects_team'), name='get_projects_team'),
    url(r'^/new_project/$', ('new_project'), name='new_project'),
    url(r'^/new_team/$', ('new_team'), name='new_team'),

    url(r'^/settings/$', ('workspace_settings'), name='settings'),
    url(r'^help/$', ('workspace_help'), name='help'),

    url(r'^(?P<name>[^/]+)/overview/$', ('overview'), name='overview'),

    url(r'^(?P<name>[^/]+)/stakeholders/$', ('stakeholders'), name='stakeholders'),    
    url(r'^(?P<name>[^/]+)/new_stakeholder/$', ('stakeholders'), name='new_stakeholder'),
    url(r'^(?P<name>[^/]+)/get_stakeholder/$', ('get_stakeholder'), name='get_stakeholder'),
    url(r'^(?P<name>[^/]+)/update_stakeholder/$', ('update_stakeholder'), name='update_stakeholder'),
    url(r'^(?P<name>[^/]+)/delete_stakeholder/$', ('delete_stakeholder'), name='delete_stakeholder'),

    url(r'^(?P<name>[^/]+)/goals/$', ('goals'), name='goals'),
    url(r'^(?P<name>[^/]+)/new_business_goal/$', ('goals'), name='new_business_goal'),    
    url(r'^(?P<name>[^/]+)/delete_business_goal/$', ('delete_business_goal'), name='delete_business_goal'),
    url(r'^(?P<name>[^/]+)/update_business_goal/$', ('update_business_goal'), name='update_business_goal'),
    url(r'^(?P<name>[^/]+)/get_business_goal/$', ('get_business_goal'), name='get_business_goal'),

    url(r'^(?P<name>[^/]+)/constraints/$', ('constraints'), name='constraints'),
    url(r'^(?P<name>[^/]+)/new_constraint/$', ('constraints'), name='new_constraint'),
    url(r'^(?P<name>[^/]+)/delete_constraint/$', ('delete_constraint'), name='delete_constraint'),
    url(r'^(?P<name>[^/]+)/update_constraint/$', ('update_constraint'), name='update_constraint'),

    url(r'^(?P<name>[^/]+)/operations/$', ('operations'), name='operations'),
    url(r'^(?P<name>[^/]+)/new_operational_scenario/$', ('operations'), name='new_operational_scenario'),
    url(r'^(?P<name>[^/]+)/delete_operational_scenario/$', ('delete_operational_scenario'), name='delete_operational_scenario'),
    url(r'^(?P<name>[^/]+)/update_operational_scenario/$', ('update_operational_scenario'), name='update_operational_scenario'),
    url(r'^(?P<name>[^/]+)/get_operational_scenario/$', ('get_operational_scenario'), name='get_operational_scenario'),

    url(r'^(?P<name>[^/]+)/utility_tree/$', ('utility_tree'), name='utility_tree'),
    url(r'^(?P<name>[^/]+)/new_utility_tree/$', ('utility_tree'), name='new_utility_tree'),
    url(r'^(?P<name>[^/]+)/update_node_score_utility_tree/$', ('update_node_score_utility_tree'), name='update_node_score_utility_tree'),
    url(r'^(?P<name>[^/]+)/update_node_utility_tree/$', ('update_node_utility_tree'), name='update_node_utility_tree'),
    url(r'^(?P<name>[^/]+)/delete_node_utility_tree/$', ('delete_node_utility_tree'), name='delete_node_utility_tree'),
    url(r'^(?P<name>[^/]+)/add_utility_tree_node/$', ('add_utility_tree_node'), name='add_utility_tree_node'),
    url(r'^(?P<name>[^/]+)/add_utility_tree/$', ('add_utility_tree'), name='add_utility_tree'),
    url(r'^(?P<name>[^/]+)/update_utility_tree/$', ('update_utility_tree'), name='update_utility_tree'),
    url(r'^(?P<name>[^/]+)/delete_utility_tree/$', ('delete_utility_tree'), name='delete_utility_tree'),

    url(r'^(?P<name>[^/]+)/quality_requirements/$', ('quality_requirements'), name='quality_requirements'),
    url(r'^(?P<name>[^/]+)/new_quality_scenario/$', ('quality_requirements'), name='new_quality_scenario'),
    url(r'^(?P<name>[^/]+)/update_quality_scenarios/$', ('update_quality_scenarios'), name='update_quality_scenarios'),
    url(r'^(?P<name>[^/]+)/get_quality_attribute_scenarios/$', ('get_quality_attribute_scenarios'), name='get_quality_attribute_scenarios'),
)