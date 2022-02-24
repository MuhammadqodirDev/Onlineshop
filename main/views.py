from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Category, Product
import datetime
from datetime import timedelta, datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def is_product_new():
    for i in Product.objects.all():
        if i not in  Product.objects.filter(created_date__gt=datetime.now() - timedelta(days=15)):
            i.new = False
            i.save()
        else:
            i.new = True
            i.save()
is_product_new()
    


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('?')[:8]
    d_products = Product.objects.all().order_by('-id')[:8]
    n_products = Product.objects.filter(new=True).order_by('?')[:8]
    

    context = {
        'products': products,   
        'categories': categories,
        'd_products': d_products,
        'n_products': n_products,
    }
    return render(request, 'index.html', context)


def products_page(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-id')
    

    # page = request.GET.get('page', 1)

    # paginator = Paginator(products, 30)
    # try:
    #     products = paginator.page(page)
    # except PageNotAnInteger:
    #     products = paginator.page(1)
    # except EmptyPage:
    #     products = paginator.page(paginator.num_pages)
    
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'products.html', context)


def login(request):
    return render(request, 'login.html')
    



def search(request):
    categories = Category.objects.all()
    if request.method == 'POST': item = request.POST.get('item')
    products_all = []
    products = Product.objects.filter(name__icontains = item)
    for q in products: products_all.append(q)
    products1 = Product.objects.filter(characters__icontains = item)
    for w in products1: products_all.append(w)
    products2 = Product.objects.filter(created_date__icontains = item)
    for d in products2: products_all.append(d)
    list1 = item.lower().split()
    for e in Category.objects.all():
        for g in list1:
            for h in e.name.split():
                if h.lower() == g: prs = Product.objects.filter(category_id=e.id); products_all.extend(prs)
    products_all = list(set(products_all))
    if len(products_all)==0: messages.info(request, 'Sorry, Nothing found for your request!')
    context = {
        'categories': categories,
        'products': products_all
    }
   
    return render(request, 'products.html', context)

    
    

def cat_filter(request, name):
    categories = Category.objects.all(); 
    category1 = Category.objects.get(name=name)
    products = Product.objects.filter(category=category1)
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'products.html', context)

    
    
