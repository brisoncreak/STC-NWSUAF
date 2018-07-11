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
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admirelog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isGood', models.BooleanField(default=True)),
                ('isFile', models.BooleanField(default=True)),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('aid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.Article')),
            ],
            options={

                'ordering': ['create_time'],
                'verbose_name': '点赞表',
                'verbose_name_plural': '点赞表',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=20)),
                ('file_size', models.IntegerField()),
                ('file_bedown', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='share/upload')),
                ('file_status', models.IntegerField(default=0)),
                ('file_beadmired', models.IntegerField(default=0)),
                ('file_benotadmired', models.IntegerField(default=0)),
                ('file_classify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Colleges')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User')),
            ],
            options={
                'verbose_name': '文件',
                'verbose_name_plural': '文件',
            },
        ),
        migrations.AddField(
            model_name='admirelog',
            name='fid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='share.File'),
        ),
        migrations.AddField(
            model_name='admirelog',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User'),
        ),
    ]
