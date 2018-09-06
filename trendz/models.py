from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfileManager(models.Manager):
	def get_queryset(self):
		return super(UserProfileManager, self).get_queryset().filter(Area="yapala")

class UserProfileManagerOne(models.Manager):
	def get_queryset(self):
		return super(UserProfileManagerOne, self).get_queryset().filter(Area="Garu/Natinga")

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	Bio = models.TextField(max_length=140, default="")
	Number = models.IntegerField(default=0)
	WhatsApp = models.IntegerField(default=0)
	Email = models.CharField(max_length=100, default="teamtrendz@gmail.com")
	Facebook = models.CharField(max_length=100, default="")
	Area = models.CharField(max_length=100, default="Garu/Natinga")
	image = models.ImageField(upload_to='profile_image', blank=True)

	area = UserProfileManager()
	info = UserProfileManagerOne()

	def __str__(self):
		return self.user.username

	


def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(username=kwargs['instance'])

post_save.connect(create_profile, sender=User)	



