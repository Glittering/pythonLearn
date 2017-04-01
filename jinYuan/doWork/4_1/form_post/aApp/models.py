from django.db import models

# Create your models here.


class People(models.Model):
    sec_ch=(
        ('male','男'),
        ('female','女')
    )
    pro_ch=(
        ('english','英语'),
        ('chinese','汉语')
    )
    nation_ch=(
        ('han','汉族'),
        ('hui','回族'),
        ('man','满族')
    )
    name = models.CharField(max_length=4, null=True, blank=True)
    sex = models.CharField(max_length=4, choices=sec_ch, null=True, blank=True)
    age = models.DateField( null=True, blank=True)
    professional = models.CharField(max_length=20,choices=pro_ch, null=True, blank=True)  #专业
    nation = models.CharField(max_length=20,choices=nation_ch, null=True, blank=True) #民族
    nation_place = models.CharField(max_length=50, null=True, blank=True) #籍贯
    education = models.CharField(max_length=20, null=True, blank=True)    #学历
    describe = models.TextField( null=True, blank=True)  #个人描述
    contact_infor = models.IntegerField( null=True, blank=True)  #联系方式(手机号)

    # sex =  单选
    # 年龄  下拉框
    # 专业  文本
    # 民族 文本
    # 籍贯  文本
    # 学历 下拉框
    # 个人描述
    # 联系方式
