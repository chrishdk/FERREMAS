# Generated by Django 5.0.6 on 2024-06-26 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='branch_name',
            field=models.CharField(default='Desconocido', max_length=100),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_description',
            field=models.TextField(default='Sin descripción'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_name',
            field=models.CharField(default='Desconocido', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]