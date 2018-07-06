from django.db import models
from index.models import *
from system.storage import ImageStorage
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
