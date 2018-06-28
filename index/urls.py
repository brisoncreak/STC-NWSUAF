from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$', index_views, name='index'),
    url(r'^login/$', index_login, name='login'),
    url(r'^logout/$', index_logout, name='logout'),
    url(r'^register/$',index_register,name='register'),
    url(r'^test/$', test),
    url(r'^modelbase/$',index_modelbase),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
'django.contrib.auth.views.password_reset_confirm',{'post_reset_redirect':'/accounts/password/reset/done/'}),
]