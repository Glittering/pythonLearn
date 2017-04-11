from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytemplate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^demo/$',demo),
    url(r'^hello/$',hello),
    url(r'^hi/$',hi),
    url(r'^index1/$',index1),
    url(r'^index2/$',index2),
    url(r'^index3/$',index3),
    url(r'^index4/$',index4),
    url(r'^first/$',first),
    url(r'^base/$',base),
    url(r'^sub/$',sub)
)
