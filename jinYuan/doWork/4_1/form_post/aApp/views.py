from django.shortcuts import render
from aApp.form import PersonalForm

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        # form.is_valid()


    elif request.method == 'GET':
        form = PersonalForm

    context = {}
    context['form'] = form
    return render(request,'index.html',context)
