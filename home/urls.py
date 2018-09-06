from django.conf.urls import url
from . import views
from home.views import HomeView

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='HomeView')
]