from django.conf.urls import patterns, include, url
from django.contrib import admin
from gjtemplate.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mygjtemplate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^hi/$',hi),
    url(r'^zy/$',zy),
    url(r'^tem_filter/$',tem_filter),
    url(r'^tem_tag/$',tem_tag)
)
