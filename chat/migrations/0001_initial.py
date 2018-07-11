# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-10 18:17

from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(default='1', max_length=30)),
                ('lable', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime.now)),
                ('is_reviewed', models.CharField(max_length=30)),
                ('reviewed_num', models.IntegerField(null=True)),
                ('skim_num', models.IntegerField(null=True)),
                ('like_num', models.IntegerField(null=True)),
                ('beadmired_num', models.IntegerField(default=0)),
                ('benotadmired_num', models.IntegerField(default=0)),
                ('reviews', models.TextField(null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Colleges')),
                ('collegetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Collegetype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User')),
            ],
            options={
                'ordering': ['skim_num'],
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=datetime.datetime.now)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User')),
            ],
            options={
                'verbose_name': '赞表',
                'verbose_name_plural': '赞表',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '评论回复表',
                'verbose_name_plural': '评论回复表',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime.now)),
                ('replys', models.TextField(null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Article')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.User')),
            ],
            options={
                'verbose_name': '文章评论表',
                'verbose_name_plural': '文章评论表',
            },
        ),
        migrations.AddField(
            model_name='reply',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Review'),
        ),
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.User'),
        ),
    ]
