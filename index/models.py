from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 100)
    create_time = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.username
    class Meta:
        #改数据库名
        #db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['username']
