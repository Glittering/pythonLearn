from django.shortcuts import render_to_response
from models import *
def index(request):
    logo =  Header_Image.objects.get(id = 1)
    search = Header_Image.objects.get(id = 2)
    ban = Banner_Image.objects.get(id = 1)
    top1 = Top_Image.objects.get(id = 1)
    top2 = Top_Image.objects.get(id = 2)
    top3 = Top_Image.objects.get(id = 3)
    left_top = Bottom_Image.objects.all()[0:3]
    left_bot1 = Bottom_Image.objects.get(id = 4)
    left_bot2 = Bottom_Image.objects.get(id = 5)
    bott = Bottom.objects.get(id = 1)
    botto= Bottom.objects.all()[1:]
    top_ol = Top_a.objects.all()
    right_top = Right_top.objects.all()
    right_bottom = Right_bottom.objects.all()
    foot_img =  Footer_Image.objects.get(id = 1)
    return render_to_response('index.html',locals())

#def base_page(request):
#    return render_to_response('base.html',locals())

def about_our(request):
    data = About.objects.get(id = 1)
    return render_to_response('about.html',locals())

def news(request):
    data = News.objects.all()
    fenye_img_zuo = New_img.objects.all()[0:2]
    fenye_img_you = New_img.objects.all()[2:4]
    return render_to_response('new.html',locals())

def jingying(request):
    data = JingYing.objects.all()[0:10]
    last_p = JingYing.objects.get(id = 11)
    return render_to_response('jingying.html',locals())

def succes(request):
    data1 = Succes.objects.get(id = 1)
    data2 = Succes.objects.all()[1:4]
    data3 = Succes.objects.get(id = 5)
    data4 = Succes.objects.all()[5:8]
    data5 = Succes.objects.get(id = 9)
    data6 = Succes.objects.all()[9:12]
    return render_to_response('succes.html',locals())

def zhiliang(request):
    data = Quality.objects.all()[0:10]
    last_p = Quality.objects.get(id = 10)
    return render_to_response('zhiliang.html',locals())

def show(request):
    data1 = Succes.objects.get(id = 1)
    data2 = Succes.objects.all()[1:4]
    data3 = Succes.objects.get(id = 5)
    data4 = Succes.objects.all()[5:8]
    data5 = Succes.objects.get(id = 9)
    data6 = Succes.objects.all()[9:12]
    return render_to_response('show.html',locals())

def contact(request):
    data = Contact.objects.all()[0:5]
    last_p = Contact.objects.get(id = 6)
    return render_to_response('contact.html',locals())

# Create your views here.
