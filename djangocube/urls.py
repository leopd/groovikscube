from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^$', 'django.views.generic.simple.redirect_to', {'url': '/sync/'}),
    (r'^sync/', include('djangocube.syncstate.urls')),

    (r'^admin/', include(admin.site.urls)),
)
