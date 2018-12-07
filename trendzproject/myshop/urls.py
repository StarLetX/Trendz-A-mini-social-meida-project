from django.conf.urls import url
from .views import products_view, new_product_view

urlpatterns = [
	url(r'^$', products_view, name="products"),
	url(r'^new$', new_product_view, name="new_product"),
]