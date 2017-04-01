from django.contrib import admin
from models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','gender']

admin.site.register(User,UserAdmin)

# Register your models here.
