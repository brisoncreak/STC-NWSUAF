from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index_views, name='market_index'),
    url(r'^ordering/(\d+)$', ordering_views, name='ordering'),
    url(r'^paying/(\d+)$', paying_views, name='paying'),
]