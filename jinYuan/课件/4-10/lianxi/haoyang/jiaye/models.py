#coding:utf-8
from django.db import models

###########################################index_page##########################################################
class Header_Image(models.Model):
    name = models.CharField(max_length = 30,verbose_name = '图片名')
    img = models.ImageField(upload_to= 'image',verbose_name = '头部图片')

    class Meta:
        verbose_name_plural = '头部图片'

class Banner_Image(models.Model):
    name = models.CharField(max_length = 30,verbose_name = '图片名')
    img = models.ImageField(upload_to= 'image',verbose_name = '导航图片')

    class Meta:
        verbose_name_plural = '导航图片'

class Top_Image(models.Model):
    name = models.CharField(max_length = 30,verbose_name = '图片名')
    img = models.ImageField(upload_to= 'image',verbose_name = '顶部图片')

    class Meta:
        verbose_name_plural = '顶部图片'

class Top_a(models.Model):
    content = models.CharField(max_length = 50)
    date = models.DateField()

    class Meta:
        verbose_name_plural = '顶部信息'

'''
class Top_li(models.Model):
    content = models.CharField(max_length = 50)
'''
class Right_top(models.Model):
    content = models.CharField(max_length = 50)
    date = models.DateField()

    class Meta:
        verbose_name_plural = '右上信息'

class Right_bottom(models.Model):
    content = models.CharField(max_length = 50)
    date = models.DateField()

    class Meta:
        verbose_name_plural = '右下信息'

class Bottom_Image(models.Model):
    name = models.CharField(max_length = 30,verbose_name = '图片名')
    img = models.ImageField(upload_to= 'image',verbose_name = '底部图片')

    class Meta:
        verbose_name_plural = '底部图片'

class Bottom(models.Model):
    img = models.ImageField(upload_to= 'image',verbose_name = '图片')
    introduce = models.CharField(max_length = 50,verbose_name = '图片简介')

    class Meta:
        verbose_name_plural = '图片'

class Footer_Image(models.Model):
    name = models.CharField(max_length = 30,verbose_name = '图片名')
    img = models.ImageField(upload_to= 'image',verbose_name = '脚部图片')

    class Meta:
        verbose_name_plural = '脚部图片'

##################################################about_our########################################################
class About(models.Model):
    title = models.CharField(max_length = 20,verbose_name = '标题')
    content = models.TextField(verbose_name = '内容')

    class Meta:
        verbose_name_plural = '关于我们'

#################################################news####################################################
class News(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateField()

    class Meta:
        verbose_name_plural = '新闻动态'

class New_img(models.Model):
    name = models.CharField(max_length = 30,verbose_name = '图片名')
    img = models.ImageField(upload_to= 'image',verbose_name = '分页图片')

    class Meta:
        verbose_name_plural = '分页图片'
#########################################jingying############################################################
'''
class Jingying(models.Model):
    title = models.CharField(max_length = 20,verbose_name = '标题')
    content = models.TextField(verbose_name = '内容')

    class Meta:
        verbose_name_plural = '经营项目'
'''
class JingYing(models.Model):
    content = models.TextField(verbose_name = '内容')

    class Meta:
        verbose_name_plural = '经营项目'
###############################################success#######################################################
class Succes(models.Model):
    img = models.ImageField(upload_to= 'image',verbose_name = '图片')
    introduce = models.CharField(max_length = 50,verbose_name = '图片简介')

    class Meta:
        verbose_name_plural = '图片案例'

################################################quality####################################################
class Quality(models.Model):
    content = models.TextField(verbose_name = '内容')

    class Meta:
        verbose_name_plural = '质量保证'
################################################contact######################################################
class Contact(models.Model):
    content = models.TextField(verbose_name = '内容')

    class Meta:
        verbose_name_plural = '联系我们'

# Create your models here.
