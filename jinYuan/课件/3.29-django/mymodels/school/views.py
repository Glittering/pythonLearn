from django.shortcuts import render_to_response
from models import *


def teacher(request):
    #data = Teacher.objects.all()
    #data = Teacher.objects.filter(age = 35)
    data = Teacher.objects.get(id = 3)
    #Teacher.objects.create(name = 'wangwang',age = 25,gender = 'female',subject = 'Chinese')
    return render_to_response('teacher.html',locals())

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template,select_template

def teach(request):
    data = Teacher.objects.all()
    #t = get_template('teacher.html')
    t = select_template(['hell.html','teaher.html','demo.html'])
    c = Context({
        'data':data
    })
    return HttpResponse(t.render(c))
# Create your views here.
