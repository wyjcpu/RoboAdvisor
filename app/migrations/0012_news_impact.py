# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20161021_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='impact',
            field=models.CharField(default=0, max_length=6),
            preserve_default=False,
        ),
    ]
