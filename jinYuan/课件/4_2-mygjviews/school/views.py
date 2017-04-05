from django.shortcuts import render_to_response

def teacher(request,a,b = 30):
    return render_to_response('teacher.html',locals())

def hello(request,name):
    return render_to_response('hello.html',locals())


# Create your views here.
