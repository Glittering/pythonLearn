from django.http import HttpResponse,HttpRequest
import time
def hello(request):
    return HttpResponse('hello world')


def hi(request):
    html = '<html><body><p style = "color:skyblue; font-size:30px;">hello world</p></body></html>'
    return HttpResponse(html)


def tm(request):
    now = time.ctime()
    html = '<html><body><h2>%s</h2></body></html>'%now
    return HttpResponse(html)

def tm1(request,num):
    now = time.time()
    num = int(num) * 3600
    thetime = time.ctime(now + num)
    html = '<html><body><p style = "color:red; font-weight:blod;">%s</p></body></html>'%thetime
    return HttpResponse(html)
