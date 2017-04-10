from django.contrib import admin
from models import *

class Header_ImageAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class Banner_ImageAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class Top_ImageAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class Bottom_ImageAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class Footer_ImageAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class AboutAdmin(admin.ModelAdmin):
    list_display = ['id','title']

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','title']

admin.site.register(Header_Image,Header_ImageAdmin)
admin.site.register(Banner_Image,Header_ImageAdmin)
admin.site.register(Top_Image,Header_ImageAdmin)
admin.site.register(Top_a)
#admin.site.register(Top_li)
admin.site.register(Right_top)
admin.site.register(Right_bottom)
admin.site.register(Bottom_Image,Header_ImageAdmin)
admin.site.register(Bottom)
admin.site.register(Footer_Image,Header_ImageAdmin)

admin.site.register(About,AboutAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(New_img)
#admin.site.register(Jingying,JingyingAdmin)
admin.site.register(JingYing)
admin.site.register(Succes)
admin.site.register(Quality)
admin.site.register(Contact)
# Register your models here.
