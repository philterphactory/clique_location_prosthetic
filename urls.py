from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       (r'^(\d+)/locations/?$',
                        'clique.views.show_group_locations'),
                       )
