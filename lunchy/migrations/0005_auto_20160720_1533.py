# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunchy', '0004_auto_20160717_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='detail',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='place',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]