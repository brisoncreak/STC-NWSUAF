# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-29 06:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20180629_0346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['create_time'], 'verbose_name': '全局通知', 'verbose_name_plural': '全局通知'},
        ),
    ]