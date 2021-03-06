# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-06 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='cod_audio',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='code audio'),
        ),
        migrations.AlterField(
            model_name='room',
            name='youtube_status',
            field=models.IntegerField(choices=[(0, 'Sem transmissão'), (1, 'Em andamento'), (2, 'Transmissão encerrada'), (3, 'Cancelada')], default=0, verbose_name='youtube status'),
        ),
    ]
