from django.conf.urls import patterns, include, url
from django.contrib import admin
from school.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mymodels.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^teacher/$',teacher),
    url(r'^teach/$',teach)
)
