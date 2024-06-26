from django.db import models

class Prices(models.Model):
    id_product = models.IntegerField(null=False,blank=False, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)