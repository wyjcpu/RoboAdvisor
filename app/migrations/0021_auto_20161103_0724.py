# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20161028_0909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rippleeffect',
            old_name='assetIdOne',
            new_name='asset_id_one',
        ),
        migrations.RenameField(
            model_name='rippleeffect',
            old_name='assetIdTwo',
            new_name='asset_id_two',
        ),
        migrations.AddField(
            model_name='assetdata',
            name='arimaeffect',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]