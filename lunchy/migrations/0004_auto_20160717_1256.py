# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunchy', '0003_auto_20160717_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='nickname',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]