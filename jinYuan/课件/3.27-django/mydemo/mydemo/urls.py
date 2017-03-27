from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^hi/$',hi),
    url(r'^tm/$',tm),
    url(r'^tm1/(\d{1,2})/$',tm1)
)
