# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-10 19:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trendz', '0007_auto_20180508_0954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Bio',
            new_name='bio',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='Number',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='image',
            new_name='profile_image',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='Area',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='Facebook',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='WhatsApp',
        ),
    ]
