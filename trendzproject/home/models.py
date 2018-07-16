# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	post = models.CharField(max_length=500)
	user = models.ForeignKey(User)
	created_date = models.DateTimeField(auto_now_add=True)
	#this allows a new date to be added if 
	#a post is updated by the user
	#this not possible now but it will
	# be added in later updates
	updated = models.DateTimeField(auto_now=True)

	