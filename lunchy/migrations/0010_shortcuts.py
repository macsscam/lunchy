# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunchy', '0009_person_fbid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shortcuts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bot_message', models.CharField(max_length=1000, unique=True)),
                ('variable_name', models.CharField(max_length=40)),
            ],
        ),
    ]
