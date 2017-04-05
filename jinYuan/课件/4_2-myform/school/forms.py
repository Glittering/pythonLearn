#coding:utf-8
from django import forms
from models import *

class RegisterForm(forms.Form):
    name = forms.CharField(
        max_length = 10,
        label = '姓名',
        error_messages = {'invalid':'This value may contain only letters'}
    )
    age = forms.IntegerField(required = False,widget = forms.PasswordInput)
    #gender =  forms.CharField(max_length = 10)
    #gender = forms.ChoiceField(choices = (('male','男'),('女','female')))
    introduce = forms.CharField(widget = forms.Textarea)
    hobby = forms.ModelMultipleChoiceField(Hobby.objects.all())
    gender = forms.MultipleChoiceField(choices = (('male','男'),('女','female')))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name[0].isdigit() == True:
            raise forms.ValidationError('首字符必须是字母')
        return name


