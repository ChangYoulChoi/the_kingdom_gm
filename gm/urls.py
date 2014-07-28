from django.conf.urls import patterns, url
from django.contrib import admin
from gm.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'the_kingdom_gm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', gm_main),
    url(r'^login/$', gm_login),
    url(r'^main/$', gm_main),
    url(r'^manager_create/$', manager_create),
    url(r'^name/$', get_name),

)
