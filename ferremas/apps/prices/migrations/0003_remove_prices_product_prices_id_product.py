# Generated by Django 5.0.6 on 2024-06-24 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0002_alter_prices_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prices',
            name='product',
        ),
        migrations.AddField(
            model_name='prices',
            name='id_product',
            field=models.IntegerField(default=0),
        ),
    ]