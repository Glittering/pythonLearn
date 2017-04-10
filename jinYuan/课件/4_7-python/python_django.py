#coding:gbk


一、请写出一个个人信息提交表单
	1、姓名 文本
	2、性别 单选
	3、年龄 下拉框	
	4、专业 文本
	5、民族 文本
	6、籍贯 文本
	7、学历 下拉框
	8、个人描述 
	9、联系方式

import python_wx
#MVC
    #M --> models 模型 the database tables 数据存储层
    #V --> views  视图 业务逻辑层
    #C --> urls   控制 有什么样的url调用什么样的视图函数

#开始一个项目
    #在CMD中切换目录
    #执行 python D:\Python27\Scripts\django-admin-script.py startproject 项目名


#import chat

#python manage.py validate 验证项目语法

#python manage.py makemigrations  生成数据库

#python manage.py syncdb 同步数据库

#python manage.py migrate 同步

#python manage.py createsuperuser 创建超级用户

#python manage.py runserver 启动项目

'''
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static').replace('\\','/'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'template').replace('\\','/'),
)
'''

#MTV
    #M --> models
    #T --> tempalte
    #v --> views

#M --> V --> template

#Queryset对象 
