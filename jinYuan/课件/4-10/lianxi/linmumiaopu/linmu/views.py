from django.shortcuts import render_to_response
from models import *


def base(request):
    return render_to_response('base.html',locals())

def index(request):
    #data = Contact.objects.all()
    #righttop1 = Introduce.objects.get(id = 1)
    #righttop2 = Introduce.objects.get(id = 2)
    #rightbot1 = Show.objects.get(id = 1)
    #rightbot2 = Show.objects.all()[1:5]
    #rightbot3 = Show.objects.get(id = 6)
    return render_to_response('index.html',locals())
'''
def jianjie(request):
    data = Contact.objects.all()
    return render_to_response('jianjie.html',locals())
'''
# Create your views here.
