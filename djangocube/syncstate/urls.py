from django.conf.urls.defaults import *

urlpatterns = patterns('syncstate.views',
    (r'^$', 'home'),
    (r'^poll$', 'poll'),
    (r'^rotate$', 'rotate'),
)
