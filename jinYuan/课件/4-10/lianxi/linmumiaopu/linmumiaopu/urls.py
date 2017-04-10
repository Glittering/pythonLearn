from django.conf.urls import patterns, include, url
from django.contrib import admin
from linmu.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'linmumiaopu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^base/$',base),
    url(r'^index/$',index),
    #url(r'^jianjie/$',jianjie)
)
