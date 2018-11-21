# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	post 			= models.CharField(max_length=100)
	user 			= models.ForeignKey(User)
	created_date	= models.DateTimeField(auto_now_add=True)
	post_image 		= models.ImageField(upload_to="post_pictures", default="default.jpg", blank=True, null=True)
	#this allows a new date to be added if
	#a post is updated by the user
	#this not possible now but it will
	# be added in later updates
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.post
