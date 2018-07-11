from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index_views, name='market_index'),
    url(r'^docs/',docs_views,name='docs_index'),
    url(r'^goods/',goods_views,name='goods_index'),
    url(r'^ordering/(\d+)$', ordering_views, name='ordering'),
    url(r'^paying/(\d+)$', paying_views, name='paying'),
    url(r'^add_good/(\d+)$', add_good_views, name='addgood'),
    url(r'^good_detail/(\d+)$', good_detail_views, name='good_detail'),
    url(r'^add_order/(\d+)$', new_order_views, name='add_order'),
    url(r'^order_view/(\d)',order_views,name="ordershow"),
    url(r'^complaint/(\d+)',complaint_views,name="complaint_page"),
    url(r'^add_tmessage/(\d+)$', add_tmessage_views, name='add_tmessage'),
    url(r'^good_list/$',good_list_views,name="goodlist"),
    url(r'^buyer_ok/(\d+)$', buyer_ok_views, name='buyer_ok'),
    url(r'^seller_ok/(\d+)$', seller_ok_views, name='seller_ok'),
    url(r'^ws/(\d+)/(\d+)$', market_ws_views),
    url(r'^cancel_order/(\d+)$', cancel_order_views,name='cancel'),
    url(r'^comment/(\d+)$', comment_views,name='comment'),
    url(r'^trade_mark/(\d+)$', trade_mark_views, name='trade_mark'),
    url(r'^add_feedback/(\d+)$', add_feedback_views, name='add_feedback'),
    url(r'^feedback/(\d+)$', feedback_views, name='feedback'),
    url(r'^cancel_fb/(\d+)$', cancel_fb_views, name='cancel_fb'),
    url(r'^add_evi/(\d+)$', add_evi_views, name='add_evi'),
    url(r'^del_good/(\d+)$', del_good_views, name='del_good'),
]