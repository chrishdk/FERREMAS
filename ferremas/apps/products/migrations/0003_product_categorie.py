# Generated by Django 5.0.6 on 2024-06-19 22:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('products', '0002_remove_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='categories.categorie'),
        ),
    ]