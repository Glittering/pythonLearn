#coding:utf-8
from django.http import HttpResponse
from django import template
import datetime

def demo(request):
    t = template.Template('my name is {{ name }},I am {{ age }} years old.') #创建模板对象
    c = template.Context({'name':'xiaoqiang','age':20})  #渲染模板
    return HttpResponse(t.render(c))  #用t加载c


def hello(request):
    t = template.Template('my name is {{ name }},I am {{ person1.age }} years old.')
    c = template.Context({
        'person1':{'name':'xiaoli','age':20},
        'person2':{'name':'laoli','age':40},
        'name_list':['zhangsan','lisi']
    })
    c['name'] = 'xiaoqiang'
    return HttpResponse(t.render(c))

def hi(request):
    html = '''
    <html>
        <head>
            <title>
                {{ title }}
            </title>
        </head>
        <body>
            <ul>
                {% for i in daohang %}
                    <li>
                        {{ i }}
                    </li>
                {% endfor %}

            </ul>
            {% if name %}
                <p>
                    hello：{{ name }}
                </p>
                <br>
                213312
            {% else %}
                <p>
                    there have no this person.
                </p>
            {% endif %}
            {% if age > 30 %}
                <p>
                    you are too old.
                </p>
            {% endif %}
            {% comment %}
                <ul>
                    {% for i in daohang %}
                        <li>
                            {{ forloop }}
                        </li>
                    {% endfor %}
                </ul>
            {% endcomment %}
            <!--
            {% ifequal age 30 %}
                <p>
                    abcdfeg
                </p>
            {% else %}
                <h2>
                    123
                </h2>
            {% endifequal %}
            -->
            <ul>
                {% for i in name_list %}
                    <li>
                        {{ i|first|upper }}
                    </li>
                {% endfor %}
            </ul>
            {{ now|date:"F j,Y" }}
        </body>
    </html>
    '''
    t = template.Template(html)
    thetime = datetime.datetime.now()
    c = template.Context({
        'title':'myworld',
        'daohang':['首页','图片','文章','音乐'],
        'name':'xiaoqiang',
        'age':31,
        'name_list':['laozhao','haojian','zhangfang','liwan'],
        'now':thetime
    })
    return HttpResponse(t.render(c))

def index1(request):
    html = open('F:\lianxi\mytemplate\\template\index.html','r')
    t = template.Template(html.read())
    c = template.Context({
        'name':'xiaoli',
        'age':20
    })
    return HttpResponse(t.render(c))

from django.template.loader import get_template
def index2(request):
    t = get_template('index.html')
    c = template.Context({
        'name':'laoli',
        'age':20
    })
    return HttpResponse(t.render(c))

from django.shortcuts import render_to_response

def index3(request):
    return render_to_response('index.html',{'name':'zhaoyang','age':20})

def index4(request):
    name = 'laozhang'
    age = 30
    return render_to_response('index.html',locals())

def first(request):
    name = 'xiaoqiao'
    age = 10
    return render_to_response('first.html',locals())

def base(request):
    return render_to_response('base.html',locals())

def sub(request):
    return render_to_response('sub.html',locals())