# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-02 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20180402_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='right_flag',
            field=models.BooleanField(default=True),
        ),
    ]
