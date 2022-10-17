from django.db import models

from shopping.models import ShoppingCart


# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    picture = models.URLField(default='https://img.freepik.com/free-vector/digital-device-mockup_53876-89354.jpg?w=826&t=st=1665647104~exp=1665647704~hmac=7acb146d6df6054b016bb1d9d70b2f2083eefaac4683cb3082cd8b4c1715ea60')
    manufacturer = models.ForeignKey('Manufacturer', null=True, on_delete=models.SET_NULL)
    categories = models.ManyToManyField(ProductCategory, related_name='products')
    cart = models.ManyToManyField(ShoppingCart, related_name='products')


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
