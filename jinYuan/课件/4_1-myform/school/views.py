from django.shortcuts import render_to_response
from models import *

def hello(request):
    return render_to_response('hello.html',locals())

def form(request):
    #name = request.POST['name']
    #name = request.POST.get('name')
    if 'name' in request.POST and request.POST['name']:
        name = request.POST['name']
    else:
        name = 0
    if 'age' in request.POST and request.POST['age']:
        age = request.POST['age']
    else:
        age = 0
    if 'gender' in request.POST and request.POST['gender']:
        gender = request.POST['gender']
    else:
        gender = 0
    if name == 0 and age == 0 or gender == 0:
        jieguo = 0
    elif name == 0 or age == 0 or gender == 0:
        jieguo = 1
    else:
        User.objects.create(name = name,age = age,gender = gender)
        jieguo = 2
    return render_to_response('form.html',locals())

# Create your views here.
