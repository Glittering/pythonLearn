from django.conf.urls import patterns, include, url
from django.contrib import admin
from jiaye.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'haoyang.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index),
    #url(r'^base_page/$',base_page),
    url(r'^about_our/$',about_our),
    url(r'^news/$',news),
    url(r'^jingying/$',jingying),
    url(r'^succes/$',succes),
    url(r'^zhiliang/$',zhiliang),
    url(r'^show/$',show),
    url(r'^contact/$',contact)
)
