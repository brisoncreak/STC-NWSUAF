# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-30 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='degree_good',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='trade_count',
            field=models.IntegerField(default=0),
        ),
    ]