from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index_views, name='market_index'),
    url(r'^docs/',docs_views,name='docs_index'),
    url(r'^goods/',goods_views,name='goods_index'),
]