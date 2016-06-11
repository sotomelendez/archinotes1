from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('Archinotes.views',
    url(r'^$', 'index', name='index'),
	url(r'^about/$', ('about'), name='about'),
    url(r'^sign_in/$', ('sign_in'), name='sign_in'),
    url(r'^sign_up/$', ('sign_up'), name='sign_up'),
)

urlpatterns += patterns('',
    (r'^management/', include('management.urls', namespace='mgmt')),
)

urlpatterns += patterns('',
    (r'^editor/', include('editor.urls', namespace='editor')),
)

urlpatterns += patterns('',
    (r'^collaboration/', include('collaboration.urls', namespace='col')),
)
