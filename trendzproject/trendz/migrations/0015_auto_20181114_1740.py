# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-11-14 17:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trendz', '0014_auto_20181110_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='area',
            new_name='location',
        ),
    ]
