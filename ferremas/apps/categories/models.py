from django.db import models

# Create your models here.
class categorie(models.Model):
    categorie = models.CharField(max_length=50)
