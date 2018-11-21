from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

'''
class UserProfileManager(models.Manager):
	def get_queryset(self):
		return super(UserProfileManager, self).get_queryset().filter(area="yapala")

class UserProfileManagerOne(models.Manager):
	def get_queryset(self):
		return super(UserProfileManagerOne, self).get_queryset().filter(area="Garu/Natinga")
'''
class UserProfile(models.Model):
	user 		  = models.OneToOneField(User, on_delete=models.CASCADE)
	bio 		  = models.TextField(default="")
	number 		  = models.IntegerField(default=0)
	location	  = models.CharField(max_length=100, default="Garu/Natinga")
	profile_image = models.ImageField(upload_to='profile_image',default="default.jpg", blank=True, null=True)
	email 		  = models.EmailField(default="")

def create_profile(sender, **kwargs):
	if kwargs["created"]:
		user_profile = UserProfile.objects.create(user=kwargs["instance"])

post_save.connect(create_profile, sender=User)

'''
	area = UserProfileManager()
	info = UserProfileManagerOne()'''

'''
def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)	'''


#**kwargs is a dictionary that stores the user values/fields
	#such as instance and methods such as created
