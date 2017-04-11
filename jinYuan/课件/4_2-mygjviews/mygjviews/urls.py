#coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from school.views import *
from demo.views import *

urlpatterns = patterns('school.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^school/(\w+)/(\d+)',include('school.urls')),
    #url(r'^teacher/(\w+)/(\d+)$','teacher'),
    #url(r'^hello/$','hello'),
    #url(r'^student/$',student),
    #url(r'^hello/$',hello,{'name':'xiaoqiang'})
)

from demo.models import *

urlpatterns += patterns('demo.views',
    url(r'^student/(?P<name>\w+)/(?P<age>\d+)$',student,{'age':50}),
    #url(r'^student/(?P<name>\w+)/(\d+)$',student)
    url(r'^man_info/$',stud_info,{'gender':'male','info':Student.objects.filter(gender = '男')},name = 'male'),
    url(r'^woman_info/$',stud_info,{'gender':'female','info':Student.objects.filter(gender = '女')}),
    url(r'^redirect/$',redirect)
)
