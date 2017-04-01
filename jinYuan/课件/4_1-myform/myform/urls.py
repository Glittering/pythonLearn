from django.conf.urls import patterns, include, url
from django.contrib import admin
from school.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^form/$',form)
)
