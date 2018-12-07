
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from trendzproject import views


urlpatterns = [

	url(r'^$', views.main_home, name="main_home"),
    url(r'^admin/', admin.site.urls),
    url(r'^trendz/', include('trendz.urls', namespace='trendz')),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^shopping/', include('myshop.urls', namespace='myshop')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
