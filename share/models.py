from django.db import models
from index.models import *
# Create your models here.
class File(models.Model):
    fileName=models.CharField(max_length=20)
    fileType=models.CharField(max_length=20)
    fileStatus=models.CharField(max_length=20)
    fileSize=models.IntegerField()
    fileBeDown=models.IntegerField()
    fileCreateTime=models.DateField()
    fileClassify=models.CharField(max_length=20)
    user=models.ForeignKey(User)