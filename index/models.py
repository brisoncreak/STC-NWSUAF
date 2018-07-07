from django.db import models
from datetime import datetime


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 100)
    email = models.EmailField(blank=True)
    create_time = models.DateTimeField(default=datetime.now)
    profile_photo = models.ImageField(upload_to='static/upload/profile_photo', blank=True, default='static/img/logo.png')
    degree_good = models.FloatField(default=0)
    good_mark = models.IntegerField(default=0)
    bad_mark = models.IntegerField(default=0)
    trade_count = models.IntegerField(default=0)

    def __str__(self):
        return self.username
    class Meta:
        #改数据库名
        #db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['create_time']
        
class Collegetype(models.Model):
    title=models.CharField(max_length=20)
    desc=models.TextField()
    # picture = models.ImageField(null=True)

    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='学院类型'
        verbose_name_plural=verbose_name

class Colleges(models.Model):

    title = models.CharField(max_length=30)
    classify = models.ForeignKey(Collegetype)
    desc = models.TextField()
    picture = models.ImageField(null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '学院/文件类型'
        verbose_name_plural = verbose_name


class Notification(models.Model):

    aim_user = models.ForeignKey(User, related_name='aim_user')
    create_time = models.DateTimeField(default=datetime.now)
    content = models.CharField(max_length = 1000)
    have_read = models.BooleanField(default=False)
    arg0 = models.IntegerField(null=True)
    arg1 = models.IntegerField(null=True)
    arg2 = models.IntegerField(null=True)
    arg3 = models.IntegerField(null=True)
    arg4 = models.ForeignKey(User, null=True)
    def __str__(self):
        return self.aim_user.username
    class Meta:
        #改数据库名
        #db_table = 'notification'
        verbose_name = '全局通知'
        verbose_name_plural = verbose_name
        ordering = ['create_time']
from chat.models import Article
from share.models import File

# 加一个点赞表　　　　目的是让点赞后刷新完　图片不刷新为未点赞状态　　而应该是一个固定的状态　
class Admirelog(models.Model):
    uid = models.ForeignKey(User)
    fid = models.ForeignKey(File,null=True)
    aid = models.ForeignKey(Article,null=True)
    isGood = models.BooleanField(default=True)
    isFile = models.BooleanField(default=True)
    create_time = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.uid
    class Meta:
        #改数据库名
        #db_table = 'notification'
        verbose_name = '点赞表'
        verbose_name_plural = verbose_name
        ordering = ['create_time']
