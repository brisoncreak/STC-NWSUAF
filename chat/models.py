from django.db import models
from datetime import datetime

from index.models import *
    
# class Block(models.Model):
#     name=models.CharField(max_length=30)
#     infor=models.TextField()
#     create_date=models.DateField(default=datetime.now)
#     article_num=models.IntegerField(null=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = '版块'
#         verbose_name_plural = verbose_name
#         ordering = ['name']

class Article(models.Model):
    topic=models.CharField(max_length=30)
    lable=models.CharField(max_length=30)
    content=models.TextField()
    create_date=models.DateTimeField(default=datetime.now)
    is_reviewed=models.CharField(max_length=30)
    reviewed_num=models.IntegerField(null=True)
    skim_num=models.IntegerField(null=True)
    like_num=models.IntegerField(null=True)
    user=models.ForeignKey(User)
    collegetype=models.ForeignKey(Collegetype) 
    college = models.ForeignKey(Colleges)
    #点赞
    beadmired_num = models.IntegerField(default=0)
    benotadmired_num = models.IntegerField(default=0)

    reviews = models.TextField(null=True)

    def __str__(self):
        return self.topic
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['skim_num']

  
class Review(models.Model):
    content=models.TextField()
    create_date=models.DateTimeField(default=datetime.now)
    user=models.ForeignKey(User,null=True)
    article=models.ForeignKey(Article)
    replys=models.TextField(null=True)

    def __str__(self):
        return self.create_date.strftime("%Y-%m-%d-%H")  
    class Meta:
        verbose_name = '文章评论表'
        verbose_name_plural = verbose_name
        

class Reply(models.Model):
    content=models.TextField()
    create_date=models.DateTimeField(default=datetime.now)
    user=models.ForeignKey(User,null=True)
    review=models.ForeignKey(Review)
    def __str__(self):
        return self.create_date.strftime("%Y-%m-%d-%H")  
    class Meta:
        verbose_name = '评论回复表'
        verbose_name_plural = verbose_name

class Like(models.Model):
    create_date=models.DateTimeField(default=datetime.now)
    user=models.ForeignKey(User)
    article=models.ForeignKey(Article)
    def __str__(self):
        return self.create_date.strftime("%Y-%m-%d-%H")  
    class Meta:
        verbose_name = '赞表'
        verbose_name_plural = verbose_name
