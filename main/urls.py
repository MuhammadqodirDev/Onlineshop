from unicodedata import name
from django.urls import path
from .views import cat_filter, index, login, products_page, search


urlpatterns = [
    path('', index, name='index'),
    path('products_page/', products_page, name='products_page'),
    path('products/<str:name>/', cat_filter, name='cat_filter'),
    path('login', login, name='login'),
    path('search/', search, name='search')
]
