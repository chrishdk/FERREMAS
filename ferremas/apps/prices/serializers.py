from rest_framework import serializers
from .models import Prices

class PricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = ['product', 'price', 'created_at']