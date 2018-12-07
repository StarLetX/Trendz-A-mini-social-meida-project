from django.conf.urls import url
from . import views
from home.views import HomeView, add

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='HomeView'),
	url(r'^add/$', add, name="create_post"),
]
