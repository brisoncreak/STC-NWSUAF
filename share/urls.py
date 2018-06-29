from django.conf.urls import url
from .views import *

urlpatterns = [
    
    url(r'^share/$',index_views, name='share_index'),

    url(r'^upload_file/$',upload_file,name='add_file'),
    url(r'^show_file/$',show_files),
    url(r'^download_file/(\d+)$',download_files,name='d_files'),
    url(r'^delete_file/(\d+)$',delete_files,name='del_files'),
]