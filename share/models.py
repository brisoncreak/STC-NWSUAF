from django.db import models
from index.models import *
from chat.models import Article

# Create your models here.
class File(models.Model):
  
    file_name=models.CharField(max_length=20)
    file_size=models.IntegerField()
    file_bedown=models.IntegerField()
    create_time=models.DateTimeField(auto_now_add=True)
    file_classify=models.ForeignKey(Colleges)
    file=models.FileField(upload_to='share/upload')
    user=models.ForeignKey(User)
    # 状态   0代表我的网盘（所有文件）　　１代表共享文件　　　２　代表付费文档
    file_status=models.IntegerField(default = 0)

    file_beadmired = models.IntegerField(default = 0)
    file_benotadmired = models.IntegerField(default = 0)

    def __str__(self):
        return self.file_name
    class Meta:
        #db_table="author"
        verbose_name='文件'
        verbose_name_plural=verbose_name

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
