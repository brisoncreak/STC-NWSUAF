from django.conf.urls import url
from .views import *
from django.contrib.auth.views import login
urlpatterns = [

    url(r'^$', index_views, name='index'),
    url(r'^login/$', index_login, name='login'),
    url(r'^logout/$', index_logout, name='logout'),
    url(r'^register/$',index_register,name='register'),
    url(r'^test/$', test),
    url(r'^modelbase/$',index_modelbase),
    url(r'^reset/$', index_reset,name='reset'),
    url(r'^back/reset/',index_back,name='back'),
    url(r'^notification/$',notify_views, name='notify'),
    url(r'^ws/$', ws_views),

    url(r'^show_goodAdmirenum/$',admire_goodnum_views,name="show_goodadmirenum"),
    url(r'^show_badAdmirenum/$',admire_badnum_views,name="show_badadmirenum"),
] 