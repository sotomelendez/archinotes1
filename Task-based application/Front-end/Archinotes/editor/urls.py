# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('editor.views',
    url(r'^(?P<name>[^/]+)/context/$', ('context'), name='context'),
    url(r'^(?P<name>[^/]+)/functional/$', ('functional'), name='functional'),
    url(r'^(?P<name>[^/]+)/information/$', ('information'), name='information'),
    url(r'^(?P<name>[^/]+)/deployment/$', ('deployment'), name='deployment'),
    url(r'^(?P<name>[^/]+)/concurrency/$', ('concurrency'), name='concurrency'),
    url(r'^(?P<name>[^/]+)/development/$', ('development'), name='development'),

    url(r'^(?P<name>[^/]+)/new_context/$', ('context'), name='new_context'),
    url(r'^(?P<name>[^/]+)/new_functional/$', ('functional'), name='new_functional'),
    url(r'^(?P<name>[^/]+)/new_information/$', ('information'), name='new_information'),
    url(r'^(?P<name>[^/]+)/new_deployment/$', ('deployment'), name='new_deployment'),
    url(r'^(?P<name>[^/]+)/new_concurrency/$', ('concurrency'), name='new_concurrency'),
    url(r'^(?P<name>[^/]+)/new_development/$', ('development'), name='new_development'),

    url(r'^(?P<name>[^/]+)/show_diagram_versions/$', ('show_diagram_versions'), name='show_diagram_versions'),

    url(r'^(?P<name>[^/]+)/new_diagram_version/$', ('canvas'), name='new_diagram_version'),

    url(r'^(?P<name>[^/]+)/edit_func/$', ('edit_func'), name='edit_func'),
    url(r'^(?P<name>[^/]+)/edit_depl/$', ('edit_depl'), name='edit_depl'),
    url(r'^(?P<name>[^/]+)/edit_info/$', ('edit_info'), name='edit_info'),

    url(r'^(?P<name>[^/]+)/canvas/$', ('canvas'), name='canvas'),
    url(r'^(?P<name>[^/]+)/add_element/$', ('canvas'), name='add_element'),
    url(r'^(?P<name>[^/]+)/update_element/$', ('canvas'), name='update_element'),
    url(r'^(?P<name>[^/]+)/delete_element/$', ('canvas'), name='delete_element'),
    url(r'^(?P<name>[^/]+)/add_connection/$', ('canvas'), name='add_connection'),
)
