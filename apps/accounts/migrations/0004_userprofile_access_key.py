# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-11 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180130_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='access_key',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
