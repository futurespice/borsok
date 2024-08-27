from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ['id', 'cart', 'address', 'status', 'created_at', 'total_price']
