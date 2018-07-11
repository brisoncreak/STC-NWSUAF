from django.conf.urls import url
from .views import *

urlpatterns=[
    url(r'^chat/$',index_views, name='chat_index'),
    url(r'^read_my/$', read_my_views,name="r_m"),
    url(r'^read_article/(\d+)$', read_article_views,name="r_a"),
    url(r'^add_article/$',add_article_views,name="a_a"),
    url(r'^add_review/(\d+)/$',add_review_views,name="a_v"),
    url(r'^add_reply/(\d+)/$',add_reply_views,name="a_p"),
    url(r'^del_article/(\d+)/$', del_article_views,name="d_a"),
    url(r'^del_review/r(\w+)u(.+)a(.+)/$', del_review_views),
    url(r'^query_article/$', query_article_views,name='articles'),
    url(r'^read_sb/(\d+)$', read_sb_views,name="r_s"),
    # url(r'^like_article/(\d+)$', like_article_views,name="l_a"),

    url(r'^kindeditor/$', file_manager),


]
