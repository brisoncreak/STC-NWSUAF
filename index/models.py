from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 100)
    email = models.EmailField(null=True)
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