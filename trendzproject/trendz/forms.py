from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
	UserCreationForm, 
	UserChangeForm, 
	PasswordChangeForm
		)



class RegistrationForm(UserCreationForm):
	Number = forms.IntegerField(required=True)

	class Meta:
		model = User

		fields = (
			'username',
			'password1',
			'password2'
			)

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.username = self.cleaned_data['username']
		user.password1 = self.cleaned_data['password1']
		user.password2 = self.cleaned_data['password2']

		if commit:
			user.save()
		
		return user



class EditProfileForm(UserChangeForm):

	class Meta:
		model = User

		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password'
			)
