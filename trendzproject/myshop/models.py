# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	name 		= models.CharField(max_length=150)
	price 		= models.DecimalField(max_digits=10, decimal_places=2)
	description = models.CharField(max_length=250)
	#Category    = models.ForeignKey(Category, related_name='products')
	#slug    	= models.SlugField(max_length=200, db_index=True)
	image 		= models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	created		= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)


	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.name

	def price_sign(self):
		strp = str(self.price)
		return strp + " GHS"
