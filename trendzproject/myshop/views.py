# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from .models import Product

from .forms import NewProductForm

# Create your views here.

def products_view(request):
	items = Product.objects.all()
	return render(request, 'myshop/products.html',  { 'items':items })


def new_product_view(request):
	if request.method == "POST":
		form = NewProductForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
		return redirect('myshop:products')
	else:
		form = NewProductForm()
	return render(request, 'myshop/new_product.html', { 'form':form })
