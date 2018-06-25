from django.db import models
from datetime import datetime
<<<<<<< HEAD
=======

>>>>>>> f409c67124a24984f39c4cb70832714b905d66bb
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 100)
<<<<<<< HEAD
    create_time = models.DateTimeField(default = datetime.now)
=======
    create_time = models.DateTimeField(default=datetime.now)
>>>>>>> f409c67124a24984f39c4cb70832714b905d66bb
    
    def __str__(self):
        return self.username
    class Meta:
        #改数据库名
        #db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['username']
