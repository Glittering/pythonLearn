#coding:utf-8
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

def fm(request):
    error = False
    username = request.POST.get('username','unkown')
    password = request.POST.get('passwd',0)

    if username[0].isdigit() == True or len(username) > 20:
        error = True
    return render_to_response('fm.html',locals())

def fm1(request):
    errors = []
    if 'username' in request.POST and request.POST['username']:
        username = request.POST['username']
        if len(username) > 20:
            errors.append('Please submit a username term 20 characters or shorter.')
        if username[0].isdigit() == True:
            errors.append('首字符必须是字母')
    return render_to_response('fm.html',locals())

from forms import RegisterForm
def register(request):
    if request.method == 'POST':
        f = RegisterForm(request.POST)
        #b = f.is_bound
        if f.is_valid():
            u = f.cleaned_data
            name = u.get('name','unkown')
    else:
        f = RegisterForm(
            initial= {'name':'xiaowang','age':25}
        )
    return render_to_response('register.html',locals())

# Create your views here.
