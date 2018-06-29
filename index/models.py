from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 100)
    email = models.EmailField(blank=True)
    create_time = models.DateTimeField(default=datetime.now)
    profile_photo = models.ImageField(upload_to='static/upload/profile_photo', blank=True, default='')
    good_mark = models.IntegerField(default=0)
    bad_mark = models.IntegerField(default=0)

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

<<<<<<< HEAD
# coding:utf-8
# from django.db import models

# Create your models here.

#省份表
class Province(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

#城市表
class City(models.Model):
    name = models.CharField(max_length=40)
    province = models.ForeignKey(Province)

    def __str__(self):
        return self.name

#这个主要是用来显示，选择的结果
class SelectP(models.Model):
    province = models.ForeignKey(Province)
    city = models.ForeignKey(City)
=======
>>>>>>> d845ad76a8b7354ff7eb270d0f232d6d39f21940
