from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index_views, name='market_index'),
    url(r'^docs/',docs_views,name='docs_index'),
    url(r'^goods/',goods_views,name='goods_index'),
    url(r'^ordering/(\d+)$', ordering_views, name='ordering'),
    url(r'^paying/(\d+)$', paying_views, name='paying'),
    url(r'^add_good/$', add_good_views, name='addgood'),
    url(r'^good_detail/(\d+)$', good_detail_views, name='good_detail'),
    url(r'^add_order/(\d+)$', new_order_views, name='add_order')
]