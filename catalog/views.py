from django.shortcuts import render
from .models import Product


def home(request):
	return render(request, 'catalog/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})