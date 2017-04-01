from django import forms
from django.core.exceptions import ValidationError


def contact_val(com):
    if len(com) != 11:
        raise ValidationError('请输入11位手机号')


class PersonalForm(forms.Form):

    name = forms.CharField(max_length=4)
    sex = forms.CharField(max_length=4)
    age = forms.DateField()
    professional = forms.CharField(max_length=20)  #专业
    nation = forms.CharField(max_length=20) #民族
    nation_place = forms.CharField(max_length=50) #籍贯
    education = forms.CharField(max_length=20)    #学历
    describe = forms.CharField(
        widget=forms.Textarea,
    )  #个人描述
    contact_infor = forms.CharField(
        validators=(contact_val,),
    )  #联系方式(手机号)
    # def clean_contact_infor(self):
    #     contact = cleaned_data['contact_infor']
    #     if len(contact) != 11:
    #         raise ValidationError('请输入11位手机号')
    #     return contact_val
