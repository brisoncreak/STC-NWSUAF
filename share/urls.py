from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^upload_file/$',upload_file),
    url(r'^show_file/$',show_files),
    url(r'^download_file/(\d+)$',download_files,name='d_files'),
]