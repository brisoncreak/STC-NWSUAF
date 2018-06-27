from django.db import models
from datetime import datetime
from index.models import User
from share.models import File

class Good(models.Model):

    pay_way_list = ((0, '支付宝'), (1, '微信'), (2, '当面交易'))

    name = models.CharField(max_length = 30)
    file = models.ForeignKey(File, null=True)
    image = models.ImageField(upload_to='static/upload/alipay', blank=True, default='')
    create_time = models.DateTimeField(default=datetime.now)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='商品价格')
    pay_way = models.IntegerField(choices = pay_way_list)
    info = models.CharField(max_length = 200)
    sell_times  = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    class Meta:
        #改数据库名
        #db_table = 'good'
        verbose_name = '商品'
        verbose_name_plural = verbose_name
        ordering = ['create_time']




class Order(models.Model):

    status_list = ((0, '等待支付'), (1, '交易完成'), (2, '投诉中'), (3, '交易取消'))
    creater = models.ForeignKey(User, null=False)
    good = models.ForeignKey(Good, null=False)
    create_time = models.DateTimeField(default=datetime.now)
    status = models.IntegerField(choices=status_list)

    def __str__(self):
        return self.create_time
    class Meta:
        #改数据库名
        #db_table = 'order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name
        ordering = ['create_time']
