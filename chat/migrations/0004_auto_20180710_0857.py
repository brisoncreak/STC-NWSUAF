# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-10 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20180710_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='topic',
            field=models.CharField(default='_', max_length=30),
        ),
    ]
