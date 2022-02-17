import asyncio
from django.shortcuts import render, redirect
from .models import Category, Product
import datetime
from datetime import timedelta, datetime


def is_product_new():
    for i in Product.objects.all():
        if i not in  Product.objects.filter(created_date__gt=datetime.now() - timedelta(days=15)):
            i.new = False
            i.save()

is_product_new()
    


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

for i in Category.objects.all():
    print(i.product.all)

def products(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-id')
    
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'products.html', context)


def login(request):
    return render(request, 'login.html')
    

def add_product(name):
    Product.objects.create(name=name)
    
    return True
    
    
