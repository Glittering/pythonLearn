#coding:utf-8
from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length = 30,verbose_name = '教师姓名')
    age = models.IntegerField(blank = True,null = True,verbose_name = '教师年龄')
    gender = models.CharField(max_length = 10)
    img = models.ImageField(upload_to = 'image',blank = True)
    subject = models.CharField(max_length = 40,verbose_name = '教授科目')
    date = models.DateField(blank = True,null = True)

    def __unicode__(self):
        return self.name

    class Meta:
        #verbose_name = '教师表'
        verbose_name_plural = '教师表'

class Student(models.Model):
    name = models.CharField(max_length = 30)
    teacher = models.ManyToManyField(Teacher)


    def __unicode__(self):
        return self.name

class Banji(models.Model):
    name = models.CharField(max_length = 50)
    teacher = models.ForeignKey(Teacher)
# Create your models here.
