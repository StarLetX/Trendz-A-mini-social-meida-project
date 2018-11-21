from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from home.forms import create_post_form
from home.models import Post

def add(request):
	if request.method == "POST":
		form = create_post_form(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			form.cleaned_data['post']
			return redirect('home:HomeView')
	else:
		form = create_post_form()
	return render(request, 'home/create_post.html', {"form": form})



class HomeView(TemplateView):
	template_name = 'home/home.html'

	def get(self, request):
		posts = Post.objects.all().order_by("-created_date")
		args = {'posts':posts}

		return render(request, self.template_name, args)
















































#===============================================================

#this form below is commented out,
#because i decided to move the post form to its own view

#=================================================================

'''
class HomeView(TemplateView):
	template_name = 'home/home.html'

	def get(self, request):
		form = HomeForm()
		posts = Post.objects.all().order_by("-created_date")
		args = {'form':form, 'posts':posts}

		return render(request, self.template_name, args)

	def post(self, request):
		form = HomeForm(request.POST)
		if form.is_valid():

			post = form.save(commit=False)
			post.user = request.user
			post.save()
			text = form.cleaned_data['post']
			form = HomeForm()
			return redirect('home:HomeView')

		args = { 'form': form, 'text': text }
		return render(request, self.template_name, args)
'''
