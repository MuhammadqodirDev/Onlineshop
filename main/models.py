from distutils.command.upload import upload
from django.core.management.base import BaseCommand
from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
import datetime
from django_extensions.db.fields import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    characters = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, related_name='product', on_delete=CASCADE)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)
    # old_price = models.PositiveIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    new  = models.BooleanField(default=True, blank=True),
    qrcode = models.ImageField(upload_to='product_qrcodes/', blank=True, null=True)
    new = models.BooleanField(default=True, null=True, blank=True)
    slug = AutoSlugField(blank=True, unique=True, populate_from=['name', 'characters', 'category', 'price', 'created_date'])

    def __str__(self):
        return self.name
    

class Brands(models.Model):
    image = models.ImageField(upload_to='brand_images/')
    name = models.CharField(max_length=30)
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name
    
    

    
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.product.name
    
    
    
