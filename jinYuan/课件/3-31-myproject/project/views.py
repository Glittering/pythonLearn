from django.shortcuts import render_to_response
from models import *

def article_base(request):
    return render_to_response('article_base.html',locals())

def article_list(request):
    data = Article.objects.all()
    return render_to_response('article_list.html',locals())

def article_content(request,id):
    article = Article.objects.get(id = int(id))
    return render_to_response('article_content.html',locals())

# Create your views here.
