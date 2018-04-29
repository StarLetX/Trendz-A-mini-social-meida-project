from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfileManager(models.Manager):
	pass

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	Bio = models.TextField(max_length=140, default="")
	Number = models.IntegerField(default=0)
	WhatsApp = models.IntegerField(default=0)
	Email = models.CharField(max_length=100, default="teamtrendz@gmail.com")
	Facebook = models.CharField(max_length=100, default="")
	Area = models.CharField(max_length=100, default="Garu/Natinga")
	image = models.ImageField(upload_to='profile_image', blank=True)

	def __str__(self):
		return self.user.username


def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(username=kwargs['instance'])

post_save.connect(create_profile, sender=User)		