from django.db import models

from shopping.models import ShoppingCart


# Create your models here.
class Profile(models.Model):
    avatar = models.URLField()
    about_me = models.TextField()
    settings = models.JSONField()

class Client(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    profile = models.ForeignKey(Profile, null=True, unique=True, on_delete=models.CASCADE, related_name='client')
    cart = models.ForeignKey(ShoppingCart, related_name='client', null=True, unique=True, on_delete=models.SET_NULL)


class Address(models.Model):
    street = models.CharField(max_length=200)
    number = models.IntegerField()
    city = models.CharField(max_length=200)
    zip = models.IntegerField()
    country = models.CharField(max_length=200)
    client = models.ForeignKey(Client, related_name='addresses', null=True, on_delete=models.SET_NULL)
