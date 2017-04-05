#coding:utf-8
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 30,verbose_name = '学生姓名')
    age = models.IntegerField(verbose_name = '学生年龄')
    gender = models.CharField(max_length = 10,verbose_name = '学生性别')
    major = models.CharField(max_length = 30,verbose_name = '所学专业')
    nation = models.CharField(max_length = 20,verbose_name = '民族')

    def __unicode__(self):
        return self.name
# Create your models here.
