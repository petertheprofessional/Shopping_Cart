from django.db import models

# Create your models here.
from products.models import Product


class ShoppingCart(models.Model):
    id = models.AutoField(primary_key=True)

