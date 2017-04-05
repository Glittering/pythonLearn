#coding:utf-8
from django.shortcuts import render_to_response

def student(request,name,age):
    return render_to_response('student.html',locals())

def stud_info(request,gender,info):
    return render_to_response('stud_info.html',locals())

from django.http import HttpResponseRedirect,Http404
from django.shortcuts import HttpResponseRedirect

def redirect(request):
    raise Http404
    #return HttpResponseRedirect('/man_info')  #重定向
# Create your views here.
