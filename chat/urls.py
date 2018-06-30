from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^admire/$', admire_views, name='index'),

]