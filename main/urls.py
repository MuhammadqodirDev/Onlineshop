from django.urls import path
from .views import index, login, products


urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('login', login, name='login')
]
