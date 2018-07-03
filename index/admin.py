from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password','degree_good','trade_count', 'good_mark', 'bad_mark']
    #添加链接
    list_display_links = ['username']
    #添加可编辑字段
    #list_editable = ['address', 'city']
    #添加搜索框
    search_fields = ['username']
    #date_hierarchy = DateField
    #右面添加过滤器
    list_filter = ['username']
    #详细页面顺序
    #fields = ('email', 'name', 'age')
    #详细页面 属性分组
    #fieldsets = (
    #    ('基本设置',{
    #       'fields':('country', 'website')
    #    }),
    #    ('高级设置',{
    #        'fields':('name', 'address','city'),
    #        'classes':('collapse',)
    #    }),
    #)
admin.site.register(User, UserAdmin)


class CollegetypeAdmin(admin.ModelAdmin):
    list_display = ['title','desc']
    list_display_links = ['title']
    search_fields = ['title']
    list_filter = ['title']
admin.site.register(Collegetype, CollegetypeAdmin)

class CollegesAdmin(admin.ModelAdmin):
    list_display = ['title','desc']
    list_display_links = ['title']
    search_fields = ['title']
    list_filter = ['title']
admin.site.register(Colleges, CollegesAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['aim_user','have_read','arg0','arg1']
    list_display_links = ['aim_user']
    #search_fields = ['title']
    #list_filter = ['title']
admin.site.register(Notification, NotificationAdmin)


