#coding:utf-8
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 50,verbose_name = '文章标题')
    author = models.CharField(max_length = 30,verbose_name = '文章作者')
    content = models.TextField(verbose_name = '文章内容')
    date = models.DateTimeField(verbose_name = '发表日期')
    introduce = models.TextField(verbose_name = '文章简介')
    type = models.CharField(max_length = 20,verbose_name = '文章类型')
    img = models.ImageField(upload_to = 'image',verbose_name = '文章图片')

    def __unicode__(self):
        return self.title

# Create your models here.
