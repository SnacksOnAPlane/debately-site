import os

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    # Django authentication pages
    (r'^login/', 'django.contrib.auth.views.login',
     {'template_name': 'auth/login.html'}),
    (r'^logout/', 'django.contrib.auth.views.logout',
     {'template_name': 'auth/logout.html'}),
    # Debately urls
    (r'^', include('debately-site.debately.urls')),
)

if settings.DEBUG:
    debately_static_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'static')
    debately_app_static_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'debately', 'static')
    urlpatterns += patterns('',    
    # the following is for service static media in the development
    # environ. Should not be used in production 
    # see http://docs.djangoproject.com/en/dev/howto/static-files/
    # for details
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': debately_static_path}),
        (r'^debately/static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': debately_app_static_path}),
    )

