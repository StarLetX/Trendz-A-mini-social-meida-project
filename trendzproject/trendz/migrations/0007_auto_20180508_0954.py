# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-08 09:54
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('trendz', '0006_auto_20180427_1457'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('area', django.db.models.manager.Manager()),
            ],
        ),
    ]
