from django.db import models

# Create your models here.

class Producto(models.Model):
    cod_producto = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    cod = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre