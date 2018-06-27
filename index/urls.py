from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$', index_views, name='index'),
    url(r'^login/$', index_login, name='login'),
    url(r'^logout/$', index_logout, name='logout'),
    url(r'^test/$', test),
    url(r'^modelbase/$',index_modelbase),
]