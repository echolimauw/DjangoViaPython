# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-11 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_auto_20190711_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
