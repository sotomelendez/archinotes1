from django.conf.urls import patterns, include, url

urlpatterns = patterns('collaboration.views',
    url(r'^settings/$', ('settings'), name='settings'),
    url(r'^create_annotation/$', ('create_annotation'), name='create_annotation'),
    url(r'^save_new_annotation_type/$', ('save_new_annotation_type'), name='save_new_annotation_type'),
    url(r'^get_all_annotation_types/$', ('get_all_annotation_types'), name='get_all_annotation_types'),
    url(r'^save_new_annotation/$', ('save_new_annotation'), name='save_new_annotation'),
    url(r'^get_all_annotations/$', ('get_all_annotations'), name='get_all_annotations'),
    url(r'^annotation_details/$', ('annotation_details'), name='annotation_details'),
)