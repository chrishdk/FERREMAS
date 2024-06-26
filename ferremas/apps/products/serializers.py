from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description','is_active']

class ProductWithPriceSerializer(serializers.ModelSerializer):
    latest_price = serializers.DecimalField(max_digits=10, decimal_places=0)
    class Meta:
        model = Product
        fields = ['id', 'name','description', 'is_active', 'latest_price']
