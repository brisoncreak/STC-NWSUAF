from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^admire/$', admire_views, name='index'),
    
    url(r'^share/$',index_views, name='share_index'),
    

    url(r'^upload_file/$',upload_file,name='add_file'),
    #已经查询完学院　　在搜索界面上传的是时候
    url(r'^upload_file2/(\w+)$',upload_file2,name='add_file2'),
    url(r'^download_file/(\d+)$',download_files,name='d_files'),
    url(r'^delete_file/(\d+)$',delete_files,name='del_files'),

    url(r'^show_College/(\w+)$',show_college,name='show_coll'),
    url(r'^show_User/(\w+)$',show_user,name='show_user'),
    url(r'^show_File/(\w+)$',show_file,name='show_file'),

]