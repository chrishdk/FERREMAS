# Generated by Django 5.0.6 on 2024-06-24 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_categorie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categorie',
        ),
    ]
