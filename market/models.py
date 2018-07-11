from django.db import models
from datetime import datetime
from index.models import User
from share.models import File


class Good(models.Model):

    pay_way_list = ((0, '支付宝'), (1, '微信'), (2, '当面交易'))

    name = models.CharField(max_length=30)
    creator = models.ForeignKey(User, verbose_name='创建者', related_name='goods')
    file = models.ForeignKey(File, blank=True, null=True)
    image = models.ImageField(upload_to='static/upload/alipay', blank=True, default='')
    create_time = models.DateTimeField(default=datetime.now)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='商品价格')
    pay_way = models.IntegerField(choices = pay_way_list)
    pay_pic = models.ImageField(upload_to='static/upload/alipay', blank=True, default='')
    info = models.CharField(max_length = 200)
    sell_times  = models.IntegerField(default=0)
    isfile = models.BooleanField(default=False)




    def __str__(self):
        return str(self.id)
    class Meta:
        #改数据库名
        #db_table = 'good'
        verbose_name = '商品'
        verbose_name_plural = verbose_name
        ordering = ['create_time']


class Order(models.Model):

    status_list = ((0, '等待支付'), (1, '等待卖家确认'),(2, '交易完成'), (3, '投诉中'), (4, '交易取消'))
    creator = models.ForeignKey(User, null=False,related_name='orders')
    good = models.ForeignKey(Good, null=False)
    create_time = models.DateTimeField(default=datetime.now)
    status = models.IntegerField(choices=status_list)
    buyer_ok = models.BooleanField(default=False)
    seller_ok = models.BooleanField(default=False)
    buyer_marked = models.BooleanField(default=False)
    seller_marked = models.BooleanField(default=False)

    def __str__(self):
         return str(self.id)
    class Meta:
        #改数据库名
        #db_table = 'order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

class Feedback(models.Model):
    fb_type = ((0, '支付问题'), (1, '其他'))
    creator = models.ForeignKey(User, null=False)
    order = models.ForeignKey(Order, null=False)
    fb_type = models.IntegerField(choices=fb_type)
    is_ongoing = models.BooleanField(default=True)
    create_time = models.DateTimeField(default=datetime.now)
    info = models.CharField(max_length = 200)
    def __str__(self):
        return str(self.id)
    class Meta:
        #改数据库名
        #db_table = 'feedback'
        verbose_name = '投诉'
        verbose_name_plural = verbose_name
        ordering = ['create_time']

class Evidence(models.Model):
    creator = models.ForeignKey(User, null=False)
    feedback = models.ForeignKey(Feedback, null=False)
    create_time = models.DateTimeField(default=datetime.now)
    content = models.ImageField(upload_to='static/upload/evidence', blank=True, default='')
    def __str__(self):
        return str(self.id)
    class Meta:
        #改数据库名
        #db_table = 'evidence'
        verbose_name = '证据'
        verbose_name_plural = verbose_name
        ordering = ['create_time']

class TradeMessage(models.Model):
    sender = models.ForeignKey(User, related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver')
    order = models.ForeignKey(Order, null=False)
    create_time = models.DateTimeField(default=datetime.now)
    content = models.CharField(max_length = 200)
    have_read = models.BooleanField(default=False)
    def __str__(self):
        return self.content
    class Meta:
        #改数据库名
        #db_table = 'trade_message'
        verbose_name = '交易消息'
        verbose_name_plural = verbose_name
        ordering = ['create_time']

class GoodRemark(models.Model):
    remark_list = ((0, '好评'), (1, '差评'))
    creator = models.ForeignKey(User, null=False)
    good = models.ForeignKey(Good, null=False)
    content = models.CharField(max_length = 200)
    remark_type = models.IntegerField(choices=remark_list)
    create_time = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.content
    class Meta:
        #改数据库名
        #db_table = 'trade_message'
        verbose_name = '商品评论'
        verbose_name_plural = verbose_name
        ordering = ['create_time']

class TradeMark(models.Model):
    mark_list = ((0, '好评'), (1, '差评'))
    creator = models.ForeignKey(User, null=False)
    order = models.ForeignKey(Order, null=False)
    content = models.CharField(max_length = 200)
    mark_type = models.IntegerField(choices=mark_list)
    create_time = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.content
    class Meta:
        #改数据库名
        #db_table = 'trade_message'
        verbose_name = '交易评论'
        verbose_name_plural = verbose_name
        ordering = ['create_time']
        