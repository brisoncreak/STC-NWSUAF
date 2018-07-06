from django.contrib import admin
from .models import *
from index.models import *
# Register your models here.
class FileAdmin(admin.ModelAdmin):
    list_display=['file_name','file_size','file_bedown','create_time','file_classify','user']
    # list_display_links=['name','age']
    # list_editable=['email']
    # search_fields=['name','email']
    # list_filter=['age']
    #fields=('email','name','age')
    # fieldsets=(
    #     ('基本设置',{
    #         'fields':('name','age','book')

    #     }),
    #     ('高级设置',{
    #          'fields':('email',),
    #          #折叠属性
    #          'classes':('collapse',)
    #     }),
    # )
admin.site.register(File,FileAdmin)
# admin.site.register(FileClassify)