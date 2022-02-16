from django.shortcuts import render, redirect
from .models import Category, Product
import datetime
from datetime import timedelta, datetime




def index(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('?')
    d_products = Product.objects.all().order_by('-discount')[:8]
    n_products = Product.objects.filter(created_date__gt=datetime.now() - timedelta(days=30))[:8]
        
    context = {
        'products': products,   
        'categories': categories,
        'd_products': d_products,
        'n_products': n_products,
    }
    return render(request, 'index.html', context)


def products(request):
    products = Product.objects.all().order_by('-id')
    
    context = {
        'products': products
    }
    return render(request, 'products.html', context)


def login(request):
    return render(request, 'login.html')
    
    
    


