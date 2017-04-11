from django.shortcuts import render_to_response
from django.template import Context,RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
'''
def hello(request):
    t = get_template('hello.html')
    c = Context({
        'name':'xiaoqiang',
        'age':20,
        'gender':'boy',
        'major':'Chinese'
    })
    return HttpResponse(t.render(c))

def hi(request):
    t = get_template('hi.html')
    c = Context({
        'name':'xiaozhao',
        'age':20,
        'gender':'girl',
        'major':'Chinese'
    })
    return HttpResponse(t.render(c))
'''
def public(request):
    return {
        'age':20,
        'major':'Chinese'
    }

def demo(request):
    return {
        'name':'xiaoli',
        'gender':'male'
    }

def hello(request):
    t = get_template('hello.html')
    c = RequestContext(request,processors = [public,demo])
    return HttpResponse(t.render(c))

#def hi(request):
#    t = get_template('hi.html')
#    c = RequestContext(request,{'name':'xiaozhang','gender':'girl'},processors = [public])
#    return HttpResponse(t.render(c))

def hi(request):
    return render_to_response(
        'hi.html',
        {'name':'laoli','gender':'girl'},
        RequestContext(request,processors = [public])
    )


def zy(request):
    name = "<script>alert('xiaoqiang')</script>"
    return render_to_response('zhuanyi.html',locals())


def tem_filter(request):
    name = 'laozhao'
    num_list = [str(i) for i in range(1,11)]
    return render_to_response('template_filter.html',locals())

def tem_tag(request):
    #current_time2 = 100
    return render_to_response('template_tags.html',locals())
# Create your views here.
