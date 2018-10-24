from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from trendz.forms import EditProfileForm, RegistrationForm


def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("home:HomeView")
		else:
			return redirect("trendz:register")
	else:
		form = RegistrationForm()
		args = {'form':form}
		return render(request, 'firstPage/register.html', args)


def view_profile(request):
	args = { 'user':request.user }
	return render(request, "accounts/profile.html", args)


def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()

			return redirect("trendz:view_profile")
	else:
		form = EditProfileForm(instance=request.user)

		args = { 'form':form }
		return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)

			return redirect("trendz:view_profile")

	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form': form}

		return render(request, 'accounts/edit_profile.html', args)
