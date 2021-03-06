# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-25 14:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bio', models.CharField(default='', max_length=140)),
                ('Number', models.IntegerField(default=0)),
                ('Email', models.CharField(default='teamtrendz@gmail.com', max_length=100)),
                ('Facebook', models.CharField(default='', max_length=100)),
                ('Area', models.CharField(default='Garu/Natinga', max_length=100)),
                ('Username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
