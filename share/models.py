from django.db import models
from index.models import *
# Create your models here.
class FileClassify(models.Model):
    title=models.CharField(max_length=20)
    desc=models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        #db_table="author"
        verbose_name='文件类型'
        verbose_name_plural=verbose_name
class File(models.Model):
    fileName=models.CharField(max_length=20)
    fileType=models.CharField(max_length=20)
    fileSize=models.IntegerField()
    fileBeDown=models.IntegerField()
    fileCreateTime=models.DateTimeField(auto_now_add=True)
    fileClassify=models.ForeignKey(FileClassify,null=True)
    file=models.FileField(upload_to='share/upload')
    user=models.ForeignKey(User,null=True)
    def __str__(self):
        return self.fileName
    class Meta:
        #db_table="author"
        verbose_name='文件'
        verbose_name_plural=verbose_name

