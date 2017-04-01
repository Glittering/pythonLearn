from django.contrib import admin
from models import *

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','subject','img']
    search_fields = ['gender','age']
    list_filter = ['date','age']
    date_hierarchy = 'date'
    ordering = ['age']
    fields = ['name','age','gender']

class StudentAdmin(admin.ModelAdmin):
    #filter_horizontal = ['teacher']
    filter_vertical = ['teacher']

class BanjiAdmin(admin.ModelAdmin):
    raw_id_fields = ['teacher']

admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Banji,BanjiAdmin)
# Register your models here.
