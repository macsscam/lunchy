# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 13:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunchy', '0010_shortcuts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shortcuts',
            new_name='Shortcut',
        ),
    ]
