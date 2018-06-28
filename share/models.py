from django.db import models
from index.models import *

class File(models.Model):
  
    file_name=models.CharField(max_length=20)
    file_type=models.CharField(max_length=20)
    file_size=models.IntegerField()
    file_bedown=models.IntegerField()
    create_time=models.DateTimeField(auto_now_add=True)
    file_classify=models.ForeignKey(Colleges,null=True)

    file=models.FileField(upload_to='share/upload')
    user=models.ForeignKey(User)
    file_status=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.fileName
    class Meta:
        #db_table="author"
        verbose_name='文件'
        verbose_name_plural=verbose_name

