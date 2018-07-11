from django.contrib import admin
from .models import *
from index.models import *
# Register your models here.
class FileAdmin(admin.ModelAdmin):
    list_display=['file_name','file_size','file_bedown','create_time','file_classify','user']

admin.site.register(File,FileAdmin)
# admin.site.register(FileClassify)


class AdmirelogAdmin(admin.ModelAdmin):
    list_display = ['uid','fid','aid','isGood','isFile']
    list_display_links = ['uid']
# uid　fid　　aid　isGood　　isFile

admin.site.register(Admirelog, AdmirelogAdmin)
