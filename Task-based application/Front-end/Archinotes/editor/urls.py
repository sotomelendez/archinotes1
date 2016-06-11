# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('editor.views',
    url(r'^(?P<name>[^/]+)/context/$', ('context'), name='context'),
    url(r'^(?P<name>[^/]+)/functional/$', ('functional'), name='functional'),
    url(r'^(?P<name>[^/]+)/information/$', ('information'), name='information'),
    url(r'^(?P<name>[^/]+)/deployment/$', ('deployment'), name='deployment'),
    url(r'^(?P<name>[^/]+)/concurrency/$', ('concurrency'), name='concurrency'),
    url(r'^(?P<name>[^/]+)/development/$', ('development'), name='development'),
    url(r'^(?P<name>[^/]+)/edit_func/$', ('edit_func'), name='edit_func'),
    url(r'^(?P<name>[^/]+)/edit_depl/$', ('edit_depl'), name='edit_depl'),
    url(r'^(?P<name>[^/]+)/edit_info/$', ('edit_info'), name='edit_info'),

    url(r'^(?P<name>[^/]+)/canvas/$', ('canvas'), name='canvas'),
)
