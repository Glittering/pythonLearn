from django.contrib import admin
from school.models import *

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    # 显示数据内容
    list_display = ['id','name','age','img']
    # 查询器
    search_fields = ['gender', 'age']
    # 右侧过滤器
    list_filter = ['date','age']
    # 数据上方的时间条
    date_hierarchy = 'date'
    # 数据排序方式
    ordering = ['age']
    # 注册页面
    fields = ['name', 'age']



class StudentAdmin(admin.ModelAdmin):
    # ManyToManyField 样式
    filter_horizontal = ['teacher']
    # What's it
    row_id_dields = ['teacher']


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Garden)
