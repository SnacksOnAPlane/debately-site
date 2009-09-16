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

