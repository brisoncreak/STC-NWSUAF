from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^market/$', market_views, name='market'),
]