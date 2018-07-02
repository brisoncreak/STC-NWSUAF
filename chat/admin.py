from django.contrib import admin
from .models import *


# class BlockAdmin(admin.ModelAdmin):
#     list_display = ['name', 'infor']
#     #添加可编辑字段
#     list_editable = ['infor']
#     #添加搜索框
#     search_fields = ['name']
#     #右面添加过滤器
#     list_filter = ['name']
    
class LikeAdmin(admin.ModelAdmin):
    list_display = ['create_date', 'user', 'article']
    #添加搜索框
    search_fields = ['user']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['topic','lable', 'create_date','is_reviewed','skim_num']
    #添加可编辑字段
    list_editable = ['lable']
    #添加搜索框
    search_fields = ['topic']
    #右面添加过滤器
    list_filter = ['topic']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['article','user', 'create_date','content']
    #添加可编辑字段
    list_editable = ['content']
    #添加搜索框
    search_fields = ['create_date']
    #右面添加过滤器
    list_filter = ['create_date']


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['review','user', 'create_date','content']
    #添加可编辑字段
    list_editable = ['content']
    #添加搜索框
    search_fields = ['create_date']
    #右面添加过滤器
    list_filter = ['create_date']


# admin.site.register(Block, BlockAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Reply, ReplyAdmin)