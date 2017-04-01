from django.conf.urls import patterns, include, url
from django.contrib import admin
from project.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^article_base/$',article_base),
    url(r'^article_list/$',article_list,name = 'hello'),
    url(r'^article_content/(\d+)/$',article_content)
)
