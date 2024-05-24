from django.db import models
from products.models import Product
from branches.models import Branch

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Cart(models.Model):
    items = models.ManyToManyField(CartItem)
